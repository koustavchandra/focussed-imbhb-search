#!/usr/bin/env python
""" 
Make a table of background for background_overlap
"""
import argparse, h5py, numpy, pycbc.results, pycbc.detector, sys
from pycbc.types import MultiDetOptionAction
import pycbc.pnutils, pycbc.events
import pycbc.version, lal
from itertools import combinations
import pandas as pd

def p_from_far(far, livetime):
    return 1 - numpy.exp(-far * livetime)

parser = argparse.ArgumentParser()
parser.add_argument("--version", action="version", version=pycbc.version.git_verbose_msg)
parser.add_argument('--statmap-file', help='HDF File containing the matched injections')
parser.add_argument('--single-trigger-files', nargs='*', help="HDF format single detector trigger files", action=MultiDetOptionAction)
parser.add_argument('--output-file')

args = parser.parse_args()

f = h5py.File(args.statmap_file,'r')
background_col, background_names = [], []

detectors = f.attrs['ifos'].split(' ')
keys = f['background_exc'].keys()
detectors_used = []
background = f['background_exc']
foreground_livetime = f.attrs['foreground_time'] / lal.YRJUL_SI
for det in detectors:
    if(det in keys):
        detectors_used.append(det)
    det_two_combo = numpy.array(list(combinations(detectors_used,2)))
    time_1, time_2 = [], []
    time_1_header = ''
    time_2_header = ''
    for i in range(len(det_two_combo)):
        time_1 = numpy.array(background[det_two_combo[i,0]+'/time'][:])
        time_2 = numpy.array(background[det_two_combo[i,1]+'/time'][:])
        time_1_header = 't_' + det_two_combo[i,0]
        time_2_header = 't_' + det_two_combo[i,1]
    cstat_rate = 1.0 / f['background_exc/ifar'][:]
    cstat_fap = p_from_far(cstat_rate, foreground_livetime)

    ids = {detector:background[detector+'/trigger_id'][:] for detector in detectors_used}
    background_cols = [background['stat'], background['ifar'], cstat_fap, time_1, time_2]
    background_names = ['Ranking Stat.', 'IFAR (yrs)', 'FAP', time_1_header, time_2_header]
    
if args.single_trigger_files:
    for ifo in args.single_trigger_files:
        f = h5py.File(args.single_trigger_files[ifo],'r')[ifo]
        ids_ifo = numpy.array(ids[ifo])
        ids_na = numpy.argwhere(ids_ifo == -1)
        snr_vals = f['snr'][:][ids_ifo]            
        chisq_vals = f['chisq'][:][ids_ifo] / (2 * f['chisq_dof'][:][ids_ifo] - 2)
        chisq_vals[ids_ifo == -1] = numpy.nan
        newsnr_vals = pycbc.events.ranking.newsnr(snr_vals, chisq_vals)
        snr = ['%.2f' % s if not numpy.isnan(s) else ' ' for s in snr_vals]
        chisq = ['%.2f' % c if not numpy.isnan(c) else ' ' for c in chisq_vals]
        newsnr = ['%.2f' % s if not numpy.isnan(s) else ' ' for s in newsnr_vals]
        
        background_names+= [ifo + "_SNR", ifo + "_CHISQ", ifo + "_NewSNR"]
        background_cols+= [snr,chisq,newsnr]

import pandas as pd
df = pd.DataFrame()
for i in range(len(background_names)):
    df[background_names[i]] = background_cols[i]
df.to_csv(args.output_file,index=False)
