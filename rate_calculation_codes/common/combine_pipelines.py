'''
Combine the found injections and generate the data release HDF5 files
The output HDF5 files are meant to contain the parameters of the injections
and also the different search false alarm probabilities
'''
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
pd.options.mode.chained_assignment = None
import logging
import argparse
import h5py, numpy
import pycbc.conversions

def hdf_append(f, key, value):
    if key in f:
        tmp = numpy.concatenate([f[key][:], value])
        del f[key]
        f[key] = tmp
    else:
        f[key] = value

log_level = logging.INFO
logging.basicConfig(level=log_level,
                        format='%(asctime)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

parser = argparse.ArgumentParser(description=__doc__)

parser.add_argument('--input-file',
                    required=True,
                    help='Path to converted XML2HDF file')
parser.add_argument('--pycbc-file',
                    required=True,
                    help='Path to PyCBC Found file')
parser.add_argument('--cwb-file',
                    required=True,
                    help='Path to cWB Found file')
parser.add_argument('--gstlal-file',
                    required=True,
                    help='Path to GstLAL Found file')
parser.add_argument('--output-file',
                    default='o3_imbhb_inj_info.h5',
                    help='Path to output_file')
parser.add_argument('--massbin',
                    required=True, type=int,
                    help = 'Mass Bin to extract')

arguments = vars(parser.parse_args())
logging.info("Parsing command line arguments...")

input_file = arguments['input_file']
pycbc_file = arguments['pycbc_file']
gstlal_file = arguments['gstlal_file']
cwb_file = arguments['cwb_file']
output_file = arguments['output_file']
massbin = float(arguments['massbin'])

logging.info('Processing Input File {}'.format(input_file))

h5files = pd.DataFrame()

with h5py.File(input_file, 'r') as f:
    for key in f['injections'].keys():
        h5files[key] = f['injections/'+key][:]
h5files.rename(columns={'alpha6' : 'massbin'}, inplace=True)
chosen = h5files[h5files['massbin'] == massbin]
chosen.reset_index(inplace=True)
chosen['Inj Time'] = chosen['tc'].round(0) # tc is the geocentric time of injection

# Matched Filter Searches provided the geocentric time of injections
# cWB provided reference time of preferred detector

logging.info('Reading PyCBC File and merging with Input File {}'.format(pycbc_file))

df_pycbc = pd.read_csv(pycbc_file, usecols=['Exc. IFAR', 'Inj Time'])
livetime = 0.74663
df_pycbc['pycbc_fap'] = 1-numpy.exp(-livetime/df_pycbc['Exc. IFAR']) # Calculating the fap value
df_pycbc = df_pycbc.round({'Inj Time': 0})
merge1 = chosen.merge(df_pycbc, on='Inj Time', how='outer') 

logging.info('Reading GstLAL File and merging with Input File {}'.format(gstlal_file))
df_gstlal = pd.read_csv(gstlal_file, 'r', delimiter=' ',header=None,names=['tc', 'gstlal_fap'])
merge2 = merge1
merge2['interval'] = numpy.nan
merge2['gstlal_fap'] = numpy.ones(merge2.shape[0])
for i in range(len(df_gstlal['tc'])):
    merge2['interval'] = merge2['tc'] - df_gstlal['tc'][i]
    index = merge2[numpy.abs(merge2['interval']) < 1].index
    merge2['gstlal_fap'][index] = df_gstlal['gstlal_fap'][i]

logging.info('Reading cWB File and merging with Input File {}'.format(cwb_file))
df_cwb = pd.read_csv(cwb_file, usecols=['Inj Time', 'cWB FAP'])
df_cwb.rename(columns={'Inj Time':'time0', 'cWB FAP': 'cwb_fap'}, inplace=True)

df = merge2
df['interval'] = numpy.nan
df['cwb_fap'] = numpy.ones(df.shape[0])
for i in range(len(df_cwb['time0'])):
    df['interval'] = df['tc'] - df_cwb['time0'][i]
    index = df[numpy.abs(df['interval']) < 1].index
    df['cwb_fap'][index] = df_cwb['cwb_fap'][i]

logging.info('Combining pipelines')    
# merge by default assign a NAN value for non-existing entries
# The below replaces those NAN with 1. (Logic: Not detected, means fap =1)
df['pycbc_fap'] = df['pycbc_fap'].fillna(1)
df['gstlal_fap'] = df['gstlal_fap'].fillna(1)

df['min_fap'] = df[['pycbc_fap','gstlal_fap', 'cwb_fap']].min(axis=1)
# Combined FAP
trials_factor = 3
df['combined_fap'] = 1 - numpy.power((1- df['min_fap']),trials_factor)    

logging.info('Storing all information to HDF5 File {}'.format(output_file))
columns = ['index', 'Exc. IFAR', 'tc_x', 'interval', 'min_fap', 'Inj Time']
key = 'injection_bin_{}/'.format(int(df['massbin'][0]))
with h5py.File(output_file, 'a') as f:
    for column in df.columns.values:
        if column in columns:
            pass
        else:
            hdf_append(f, key + column, df[column])            

logging.info('Finished!')