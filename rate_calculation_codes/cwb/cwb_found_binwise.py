#!/usr/bin/python
"""
Extract cWB injections and store then bin wise
"""

import argparse
import logging
import pandas as pd
import numpy
from pycbc.cosmology import _redshift
import pycbc.conversions

logging.basicConfig(format='%(asctime)s %(message)s',
                    level=logging.INFO)

parser = \
    argparse.ArgumentParser(description='Disentangle cWB injections based on bin number'
                            )

parser.add_argument('--input-file',
                    help='CSV File containing the matched injections')
parser.add_argument('--bin-number', help='Bin number to extract',
                    type=int, default=0)
parser.add_argument('--output-file', type=str, default='try.csv',
                    help='Name of the output frame file')
parser.add_argument('--cwb-livetime',type=float,default=0.7343,
                    help='cWB Search Livetime')

arguments = vars(parser.parse_args())
logging.info('Parsing command line arguments...')

input_file = arguments['input_file']
bin_number = int(arguments['bin_number'])
output_file = str(arguments['output_file'])
cwb_livetime=float(arguments['cwb_livetime'])

logging.info('Injections of bin {} are being extracted'.format(bin_number))
logging.info('Reading CSV File...')
df = pd.read_csv(input_file, sep=' ')
df1 = df[df.massbin == bin_number]

# Adding some extra columns for Koustav's benefit (normalising conventions etc...)

df2 = pd.DataFrame()
df2['Exc. IFAR'] = pycbc.conversions.sec_to_year(df1.ifar)
df2['cWB FAP'] = 1 - numpy.exp(-cwb_livetime/df2['Exc. IFAR'])
df2['Inj Time'] = df1['time0']
df2['massbin'] = df1['massbin']

df2['chi_eff'] = \
    numpy.round(pycbc.conversions.chi_eff(spin1z=df1['spin1z'],
                                          spin2z=df1['spin2z'], 
                                          mass1=df1['mass1'],
                                          mass2=df1['mass2']), 2)

df2['chi_p'] = numpy.round(pycbc.conversions.chi_p(spin1x=df1['spin1x'],
                                                   spin1y=df1['spin1y'],
                                                   spin2x=df1['spin2x'],
                                                   spin2y=df1['spin2y'],
                                                   mass1=df1['mass1'],
                                                   mass2=df1['mass2'],), 2)

df2['mtotal'] = pycbc.conversions.mtotal_from_mass1_mass2(df1['mass1'],
                                                          df1['mass2'])

df2['q'] = numpy.round(pycbc.conversions.q_from_mass1_mass2(df1['mass1'],
                                                            df1['mass2']),2)

df2 =df2[df2['Exc. IFAR'] !=0]

logging.info('Writing to file {}'.format(output_file))
df2.to_csv(output_file,
           index=False)