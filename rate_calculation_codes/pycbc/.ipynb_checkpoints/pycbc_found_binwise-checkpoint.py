#!/usr/bin/python
"""
Find found injections of particular type in the CSV file
"""
import argparse, logging, pandas as pd

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

parser = argparse.ArgumentParser(description='Returns the number of injections abover an IFAR threshold')
parser.add_argument('--input-file', 
                    help='CSV File containing the matched injections')
parser.add_argument('--mtotal', 
                    help='Source frame total mass of the system', 
                    type=float, default=800.)
parser.add_argument('--mratio', 
                    help='Mass ratio of the system (convention is that q=m1/m2)', 
                    type=float, default=1.)
parser.add_argument('--chieff', 
                    help='Effective total spin', type=float, default=0.)
parser.add_argument('--chip', 
                    help='Effective precession', type=float, default=0.)
parser.add_argument('--mass-bin',
                    type=int, default=0)
parser.add_argument('--output-dir', type=str, help='Output Directory', default='found_binwise')

arguments = vars(parser.parse_args())
logging.info("Parsing command line arguments...")

input_file = arguments['input_file']
output_dir = arguments['output_dir']
total_mass = float(arguments['mtotal'])
mratio = float(arguments['mratio'])
chi_eff = float(arguments['chieff'])
chi_p = float(arguments['chip'])
massbin = int(arguments['mass_bin'])

logging.info("Injections parameters requested: Total-Mass {}, chip {}, chieff {}, mass-ratio {}".format(total_mass, chi_p, chi_eff, mratio))
logging.info("Reading CSV File...")
df = pd.read_csv(input_file)

rslt_df = df[df.source_mass > (total_mass - 5)]
rslt_df = rslt_df[rslt_df.source_mass < (total_mass + 5)]

rslt_df = rslt_df[rslt_df.q >= (mratio - 0.3)]
rslt_df = rslt_df[rslt_df.q <= (mratio + 0.3)]

rslt_df = rslt_df[rslt_df.chip >= (chi_p - 0.2)]
rslt_df = rslt_df[rslt_df.chip <= (chi_p + 0.2)]

rslt_df = rslt_df[rslt_df.chieff >= (chi_eff - 0.2)]
rslt_df = rslt_df[rslt_df.chieff <= (chi_eff + 0.2)]
rslt_df['massbin'] = massbin 

logging.info('Writing to file {}'.format(massbin))
output_file = output_dir +'/pycbc_bin_number_' + str(massbin) + '.csv'
rslt_df.to_csv(output_file, index = False)
logging.info('Finished!')