#!/usr/bin/python
"""
Find found injections of particular type in the CSV file
"""
import argparse, logging, pandas as pd, os

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

parser = argparse.ArgumentParser(description='Returns the number of injections abover an IFAR threshold')

parser.add_argument('--input-file', 
                    help='CSV File containing the matched injections')
parser.add_argument('--output-dir', type=str, help='Output Directory', default='found_binwise')

arguments = vars(parser.parse_args())
logging.info("Parsing command line arguments...")

input_file = arguments['input_file']
output_dir = arguments['output_dir']

ext = os.path.splitext(input_file)[-1].lower()
massbin = int(''.join(filter(str.isdigit, input_file)))
logging.info('Saving info of mass bin {}'.format(massbin))
df = pd.read_csv(input_file, 'r', delimiter=' ',header=None,names=['Inj Time', 'GstLAL FAP'])
df = df[df['GstLAL FAP'] !=1.]
output_file = output_dir + '/gstlal_bin_{}'.format(massbin) + '.csv'
df.to_csv(output_file,index=False)
logging.info('Done!')