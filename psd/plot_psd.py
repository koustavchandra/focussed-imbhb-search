### Importing Requisite Modules

import pylab
import seaborn as sns
from six.moves import range
import h5py, numpy
import matplotlib

### Making figures better looking
sns.set_style("white")
sns.set_context("talk")
sns.set_palette('colorblind')

matplotlib.rcParams.update(
    {
        'text.usetex': False,
        'font.family': 'stixgeneral',
        'mathtext.fontset': 'stix',
    }
)

# Read noise data
print("Reading noise data ...")

psd_directory = '/home/koustav.chandra/o3_dev_ops/psds/output/psds'
H1_noise_data = numpy.loadtxt(psd_directory + '/H1-AVERAGE_PSD-1258642818-28800.txt')
H1_freq = H1_noise_data[:,0]
H1_psd = H1_noise_data[:,1]

L1_noise_data = numpy.loadtxt(psd_directory + '/L1-AVERAGE_PSD-1258642818-28800.txt')
L1_freq = L1_noise_data[:,0]
L1_psd = L1_noise_data[:,1]

V1_noise_data = numpy.loadtxt(psd_directory + '/V1-AVERAGE_PSD-1258642818-28800.txt')
V1_freq = V1_noise_data[:,0]
V1_psd = V1_noise_data[:,1]

print("Asserting frequencies ...")
for H1_f, L1_f,V1_f in zip(H1_freq, L1_freq,V1_freq):
    assert H1_f == L1_f == V1_f

### Harmonic Mean
print("Calculating Average PSD")
sum_inv_psds = 1./H1_psd + 1./L1_psd + 1./V1_psd
avg_psd = 3./sum_inv_psds
network_psd = numpy.vstack((H1_freq, avg_psd)).T

numpy.savetxt('H1L1V1-AVERAGE_PSD-1258642818-28800.txt',network_psd)

print("Plotting PSDs")
pylab.figure(figsize=(15,8))
pylab.loglog(H1_freq, H1_psd, label='H1')
pylab.loglog(L1_freq, L1_psd, label='L1')
pylab.loglog(V1_freq, V1_psd, label='V1')
pylab.loglog(H1_freq, avg_psd, color='deepskyblue', label ='H1L1V1')
pylab.legend()
pylab.xlim(10., 4096.)
pylab.ylim(1e-50, 1e-37)
pylab.xlabel('Frequency (Hz)')
pylab.ylabel('Power Spectral Density (Strain / Hz)')
pylab.savefig('O3_24Nov_PSD.png',dpi =100, bbox_inches='tight')
print("Done!")
