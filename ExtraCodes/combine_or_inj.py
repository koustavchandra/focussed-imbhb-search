"""Collect injection results from different pipelines into a single file.
Significances are expressed in terms of FAP"""

from __future__ import division
import numpy
import pandas as pd
import argparse, logging
pd.options.mode.chained_assignment = None 

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

parser = argparse.ArgumentParser(description='Returns the number of injections recovered below a particular FAP threshold')

parser.add_argument('--pycbc-bin-file',
                    help='CSV File containing the PyCBC injections', 
                    required = True)
parser.add_argument('--cwb-bin-file',
                    help='CSV File containing the cWB injections',
                    required = True )
parser.add_argument('--gstlal-bin-file', 
                    help='CSV File containing GstLAL injections')
parser.add_argument('--fap-threshold',
                    help='Exclusive FAP threshold', type=float, default=0.194)
parser.add_argument('--output-file',
                    type=str, 
                    default='try.csv',
                    help='Name of the output frame file')

arguments = vars(parser.parse_args())
logging.info("Parsing command line arguments...")

pycbc_bin_file = arguments['pycbc_bin_file']
gstlal_bin_file = arguments['gstlal_bin_file']
cwb_bin_file = arguments['cwb_bin_file']
fap_threshold = float(arguments['fap_threshold'])
output_file = arguments['output_file']

# Reading two columns of the CSV Files and rounding Inj Time to nearest sec
logging.info("Reading CSV Files...")
df_cwb = pd.read_csv(cwb_bin_file, usecols=['Inj Time', 'Exc. FAP', 'massbin'])
df_cwb = df_cwb.round({'Inj Time': 0})
df_cwb = df_cwb.rename(columns={'Exc. FAP': 'cWB FAP'})

print('MassBin Number ',df_cwb['massbin'][0])
# Replacing cWB 0s by numpy.nan ---> 0 == Not Found for cWB
df_cwb['cWB FAP'] = df_cwb['cWB FAP'].where(df_cwb['cWB FAP']!=0., numpy.nan) 

# Reading two columns of the CSV Files and rounding Inj Time to nearest sec
df_pycbc = pd.read_csv(pycbc_bin_file, usecols=['Inj Time', 'Exc. IFAR'])
df_pycbc = df_pycbc.round({'Inj Time': 0})
# Recalculating PyCBC FAP with combined analysis time. The same is done for candidate events
analysis_time_pycbc = 0.74663
df_pycbc['PyCBC FAP'] = 1-numpy.exp(-analysis_time_pycbc/df_pycbc['Exc. IFAR'])


# Reading two columns of the CSV Files and rounding Inj Time to nearest sec
df_gstlal = pd.read_csv(gstlal_bin_file, 'r', delimiter=' ',header=None,names=['Inj Time', 'GstLAL FAP'])
df_gstlal = df_gstlal.round({'Inj Time': 0})

# Union of the dataframe with Inj Time as key. 
# For details check this page: https://stackoverflow.com/questions/53645882/pandas-merging-101
df = df_cwb
df = df.merge(df_pycbc, on = 'Inj Time', how='outer').merge(df_gstlal, on='Inj Time', how='outer')

df = df.drop_duplicates() # This line is for sanity. 

# If any entry is NaN, the min drops it.
# For details check this page: https://stackoverflow.com/questions/44304419/max-min-of-date-column-in-pandas-columns-include-nan-values
df['min FAP'] = df[['cWB FAP','PyCBC FAP', 'GstLAL FAP']].min(axis=1)
# Combined FAP
trials_factor = 3
df['Combined FAP'] = 1 - numpy.power((1- df['min FAP']),trials_factor)

# Extracting injections with FAP less than threshold
rslt_df = df[df['Combined FAP'] <= fap_threshold]
logging.info('Writing to file {}'.format(output_file))
rslt_df.to_csv(output_file, index=False)
print("Number of common injections with FAP less than {}: {}".format(fap_threshold, len(rslt_df)))
logging.info('Finished!')
