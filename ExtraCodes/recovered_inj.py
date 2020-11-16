#!/usr/bin/python
"""
Find number of injections in a given block above a certain IFAR threshold.
"""
import argparse, logging, pandas as pd

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

parser = argparse.ArgumentParser(description='Returns the number of injections abover an IFAR threshold')
parser.add_argument('--input-file', 
                    help='HDF File containing the matched injections')
parser.add_argument('--mtotal', 
                    help='Source frame total mass of the system', 
                    type=float, default=800.)
parser.add_argument('--mratio', 
                    help='Mass ratio of the system (convention is that q=m1/m2)', 
                    type=float, default=1.)
parser.add_argument('--chieff', 
                    help='Effective spin', type=float, default=0.)
parser.add_argument('--chip', 
                    help='Effective precession', type=float, default=0.)
parser.add_argument('--ifar', 
                    help='Exclusive IFAR threshold', type=float, default=2.94)
parser.add_argument('--output-file', type=str, default='try.csv',
                   help='Name of the output frame file')

arguments = vars(parser.parse_args())
logging.info("Parsing command line arguments...")

input_file = arguments['input_file']
total_mass = float(arguments['mtotal'])
mratio = float(arguments['mratio'])
chi_eff = float(arguments['chieff'])
chi_p = float(arguments['chip'])
ifar = float(arguments['ifar'])
output_file = str(arguments['output_file'])

logging.info("Injections parameters requested: Total-Mass {}, chip {}, chieff {}, mass-ratio {}".format(total_mass, chi_p, chi_eff, mratio))
logging.info("Reading CSV File...")
df = pd.read_csv(input_file)

rslt_df = df[df.source_mass > (total_mass - 1)]
rslt_df = rslt_df[rslt_df.source_mass < (total_mass + 1)]

rslt_df = rslt_df[rslt_df.q >= (mratio - 0.1)]
rslt_df = rslt_df[rslt_df.q <= (mratio + 0.1)]

rslt_df = rslt_df[rslt_df.chip >= (chi_p - 0.1)]
rslt_df = rslt_df[rslt_df.chip <= (chi_p + 0.1)]

rslt_df = rslt_df[rslt_df.chieff >= (chi_eff - 0.1)]
rslt_df = rslt_df[rslt_df.chieff <= (chi_eff + 0.1)]
rslt_df = rslt_df[rslt_df['Exc. IFAR'] >= ifar]

logging.info("Number of injections with IFAR. greater than {} in this file: {}".format(ifar, len(rslt_df)))
logging.info('Finished!')