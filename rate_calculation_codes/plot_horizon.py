#!/usr/bin/python
'''
Plot Horizon Distance
'''

import matplotlib
matplotlib.use('Agg')
import seaborn as sns, pylab

sns.set_context('talk')
sns.set(font_scale=1.7)
sns.set_palette('colorblind')
sns.set_style('whitegrid')

pylab.rcParams.update({'text.usetex': False,
                      'font.family': 'stixgeneral',
                      'mathtext.fontset': 'stix'})

pylab.rcParams['axes.linewidth'] = 1

colors = ['#d7191c', '#fdae61', '#abd9e9', '#2c7bb6']

import pycbc, h5py, numpy, sys, os, math
from pycbc.waveform import get_fd_waveform, fd_approximants
from pycbc.filter import sigma
from pycbc.types import FrequencySeries
from pycbc import distributions
from pycbc.psd import aLIGOZeroDetHighPower
from pycbc.filter import match, sigmasq
import pycbc.conversions as conversions
import pandas as pd
import argparse, logging

from mpl_toolkits.mplot3d import Axes3D, proj3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection # New import


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--version', action='version',
                    version=pycbc.version.git_verbose_msg)
parser.add_argument('--psd-files', nargs='+', help='txt file of psds')
parser.add_argument('--ifos', nargs='+', help='Name of ifos')
parser.add_argument('--output-file', help='output file name')
parser.add_argument('--min-mtotal', help='Minimum total mass for range'
                    , type=float)
parser.add_argument('--max-mtotal', help='Maximum total mass for range'
                    , type=float)
parser.add_argument('--d-mtotal', help='Delta total mass for range ',
                    type=float)
parser.add_argument('--approximant',
                    help='Frequency domain approximant to use')
parser.add_argument('--min-spin', help='minimum dimensionless spin', type=float)
parser.add_argument('--max-spin', help='maximum dimensionless spin', type=float)
parser.add_argument('--d-spin', help='Delta spin for range ',
                    type=float)
parser.add_argument('--low-frequency-cutoff',
                    help='Lower frequency cutoff', type=float, default=10.)
parser.add_argument('--canonical-snr', help='SNR Threshold',
                    type=float, default=8.0)

args = parser.parse_args()

log_level = logging.INFO  # if opts.verbose else logging.WARN
logging.basicConfig(level=log_level, format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

if args.approximant not in fd_approximants():
    logging.info('Currently time domain waveforms are not supported')
    sys.exit()

if args.min_spin != None and args.max_spin != None:
    if args.min_spin < -1 or args.max_spin > 1:
        logging.info('Currently supports only CBC waveforms')
        sys.exit()

if len(args.psd_files) != len(args.ifos):
    logging.info('Number of ifos donot match with the number of psd files'
                 )
    sys.exit()

def get_horinzon_distance(
    approximant,
    mass,
    psd,
    f_low,
    delta_f,
    spin=0,
    canonical_snr=args.canonical_snr,
    ):
    logging.info('Trying injection with mass {:.2f}, spin {:.2f}'.format(mass,
                 spin))
    (injection_waveform_plus, _) = get_fd_waveform(
        approximant=approximant,
        mass1=mass / 2.,
        mass2=mass / 2.,
        spin1z=spin,
        spin2z=spin,
        delta_f=delta_f,
        f_lower=f_low,
        distance=1,
        )

    flen = min(len(injection_waveform_plus), len(psd))
    injection_waveform_plus.resize(flen)

    sigma = pycbc.filter.sigma(injection_waveform_plus, psd=psd,
                               low_frequency_cutoff=f_low)

    horizon_distance = sigma / canonical_snr
    return horizon_distance

def countDigit(n):
    return math.floor(math.log10(n)+1)
 
if args.min_spin == None and args.max_spin == None:
    fig = pylab.figure(figsize=(15, 12))
else:
    fig = pylab.figure(figsize=(15, 12))
    ax = pylab.axes(projection ="3d")

colors = {'H1':'#1e81b0', 
          'L1':'#e28743', 
          'V1':'#eab676', 
          'K1':'#76b5c5', 
          'I1':'#21130d', 
          'CE1':'#873e23',
          'CE2':'#abdbe3',
          'Einstein': '#063970',
          'Voyager':'#154c79'}

red_patch = []
k=0
for psd_file in args.psd_files:
    td_length = 2048  # seconds
    srate = 4096  # Hz
    N = int(td_length * srate)
    fd_length = int(N / 2 + 1)
    delta_t = 1.0 / srate
    delta_f = 1.0 / td_length
    f_low = args.low_frequency_cutoff

    logging.info('Reading PSD of %s detector', args.ifos[k])
    psd = pycbc.psd.from_txt(psd_file, length=fd_length,
                             delta_f=delta_f, low_freq_cutoff=f_low,
                             is_asd_file=True)

    if args.min_spin == None and args.max_spin == None:
        i = 0
        df = pd.DataFrame(columns=['mtotal', 'horizon_distance'])  # Creating it for easy saving
        for mass in numpy.arange(args.min_mtotal, args.max_mtotal,
                                 args.d_mtotal):
            horizon_distance = get_horinzon_distance(
                approximant=args.approximant,
                mass=mass,
                psd=psd,
                f_low=f_low,
                delta_f=delta_f,
                spin=0,
                )

            df.loc[i, 'mtotal'] = mass
            df.loc[i, 'horizon_distance'] = horizon_distance
            i = i + 1

        df['inspiral_range'] = df['horizon_distance'] / 2.26
        logging.info('Plotting')
        mbin = df['mtotal'].to_list()
        hdist = df['horizon_distance'].to_list()
        pylab.fill_between(mbin, 0, hdist, color = colors[args.ifos[k]])
        pylab.xlabel('Total Mass in Source Frame [M$_{\odot}$]')
        pylab.ylabel('Horizon Distance [Mpc]')
        pylab.yscale('log')
        pylab.xscale('log')
        #pylab.ylim(10, numpy.power(10,countDigit(numpy.max(hdist))))
        pylab.xlim(args.min_mtotal, args.max_mtotal)
    
    else:
        i = 0
        df = pd.DataFrame(columns=['mtotal', 'horizon_distance',
                          'inspiral_range', 'chi_eff'])
        for mass in numpy.arange(args.min_mtotal, args.max_mtotal,
                                 args.d_mtotal):
            for spin in numpy.arange(args.min_spin, args.max_spin,
                    args.d_spin):
                horizon_distance = get_horinzon_distance(
                    approximant=args.approximant,
                    mass=mass,
                    psd=psd,
                    f_low=f_low,
                    delta_f=delta_f,
                    spin=spin,
                    )

                df.loc[i, 'mtotal'] = mass
                df.loc[i, 'chi_eff'] = \
                    pycbc.conversions.chi_eff(mass1=mass / 2, mass2=mass / 2,
                        spin1z=spin, spin2z=spin)
                df.loc[i, 'horizon_distance'] = horizon_distance
                i = i + 1
                
        df['inspiral_range'] = df['horizon_distance'] / 2.26
        logging.info('Plotting')
        x, y, z = df['mtotal'].to_list(), df['chi_eff'].to_list(), df['horizon_distance'].to_list()
        # Creating plot
        ax.plot_trisurf(x, y, z, color = colors[args.ifos[k]], edgecolor='none')
        #ax.scatter3D(x, y, z, color=colors[k], label=args.ifos[k])
        ax.set_xlabel('Total Mass in Source Frame [M$_{\odot}$]',labelpad=10)
        ax.set_zlabel('Horizon Distance [Mpc]', labelpad=15)
        ax.set_ylabel(r'$\chi_{eff}$',labelpad=15)
        ax.set_xlim(args.min_mtotal, args.max_mtotal)
        #ax.set_xscale('log')
        #ax.set_zscale('log')
        ax.set_ylim(-1, 1)
        #ax.set_zlim(10, numpy.power(10,countDigit(numpy.max(hdist))))
    k = k + 1

for ifo in args.ifos:
    red_patch.append(matplotlib.patches.Patch(color=colors[ifo], label=ifo))

pylab.legend(handles=red_patch, loc='upper left')
fig.savefig(args.output_file, dpi=100, bbox_inches='tight')
logging.info('Done!')
