import argparse, h5py, numpy, pycbc.results, pycbc.detector, sys
from pycbc.types import MultiDetOptionAction
import pycbc.pnutils, pycbc.events
import pycbc.version, logging
from itertools import combinations
import pandas as pd
from pycbc.cosmology import _redshift

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

parser = argparse.ArgumentParser(description='Combine multiple injfind files')
parser.add_argument('--injection-files', 
                    help='HDF File containing the matched injections',
                    nargs='+')
parser.add_argument('--output-file', type=str, default='default.csv',
                   help='Name of the output frame file')
parser.add_argument('--pycbc-livetime', 
                    help='Live Time of PyCBC Search', type=float, default=0.74663)

arguments = vars(parser.parse_args())
logging.info("Parsing command line arguments...")

injection_files = arguments['injection_files']
output_file = str(arguments['output_file'])
livetime = float(arguments['pycbc_livetime'])

final_df = pd.DataFrame()

for inj in injection_files:
    logging.info("Reading Injection Information of file {}".format(inj))
    f = h5py.File(inj,'r')
    inj = f['injections']
    found_cols, found_names, found_formats = [], [], []
    logging.info("Analysing Found after vetoes injections of the file ...")
    title = "Found Injections"
    found = f['found_after_vetoes']
    idx = found['injection_index'][:]
    keys = f['found_after_vetoes'].keys()
    found = f['found_after_vetoes']
    found_cols = [found['stat'], found['ifar_exc']]
    found_names = ['Ranking Stat.', 'Exc. IFAR'] 

    m1, m2 = inj['mass1'][:][idx], inj['mass2'][:][idx]
    s1x, s1y, s1z = inj['spin1x'][:][idx], inj['spin1y'][:][idx], inj['spin1z'][:][idx]
    s2x, s2y, s2z = inj['spin2x'][:][idx], inj['spin2y'][:][idx], inj['spin2z'][:][idx]
    inj_time = inj['end_time'][:][idx]
    dist = inj['distance'][:][idx]

    z = _redshift(distance=dist)
    mtotal = pycbc.conversions.mtotal_from_mass1_mass2(m1,m2)
    q = numpy.round(pycbc.conversions.q_from_mass1_mass2(m1,m2),2)

    chip = numpy.round(pycbc.conversions.chi_p(spin1x=s1x, 
                                   spin1y=s1y,
                                   spin2x=s2x, 
                                   spin2y=s2y,
                                   mass1=m1,
                                   mass2=m2),2)

    chieff = numpy.round(pycbc.conversions.chi_eff(spin1z=s1z,
                                       spin2z=s2z,
                                       mass1=m1,
                                       mass2=m2),2)

    columns = [mtotal, q, z, chip, chieff, inj_time] + found_cols
    names = ["mtotal", "q", "z", "chip", "chieff", 'Inj Time'] + found_names

    df1 = pd.DataFrame() 
    for i in range(len(names)):
        df1[names[i]] = columns[i]

    df1['source_mass'] = numpy.round(df1.mtotal/(1 + df1.z),2) # Adding source frame total mass in column
    
    if final_df.empty:
        final_df = df1
    else:
        final_df = final_df.append(df1, ignore_index=True)        

final_df['PyCBC FAP'] = 1-numpy.exp(-livetime/final_df['Exc. IFAR'])        
logging.info('Saving data as CSV ...')
final_df.to_csv(output_file, index=False)
logging.info('Finished!')
