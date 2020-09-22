# This is the script run to create the PhaseTD statistic histograms for signal
# rate calculation. These files are stored on CVMFS under:
# /cvmfs/oasis.opensciencegrid.org/ligo/sw/pycbc/statistic-files/v2/


declare -a ifos=('L1' 'H1' 'V1')
three_ifo_sample_size=80000000
two_ifo_sample_size=8000000
batch_size=2000000
snr_ratio=3.0
seed=10
snr_reference=4
snr_uncertainty=1
weight_threshold=0.0001

three_ifo_timing_uncertainty=0.002
two_ifo_smoothing_sigma=3
three_ifo_smoothing_sigma=2
two_ifo_bin_density=4
three_ifo_bin_density=2
two_ifo_pb_dtype=int32
three_ifo_pb_dtype=int8

# LV
pycbc_multiifo_dtphase \
      --ifos L1 V1 \
      --relative-sensitivities 1 0.3 \
      --sample-size ${two_ifo_sample_size} \
      --batch-size ${batch_size} \
      --snr-ratio ${snr_ratio} \
      --seed ${seed} \
      --snr-reference ${snr_reference} \
      --output-file L1V1-stat.hdf \
      --timing-uncertainty 0.002 \
      --smoothing-sigma ${two_ifo_smoothing_sigma} \
      --snr-uncertainty ${snr_uncertainty} \
      --weight-threshold ${weight_threshold} \
      --bin-density ${two_ifo_bin_density} \
      --param-bin-dtype ${two_ifo_pb_dtype} \
      --verbose

# HV 
pycbc_multiifo_dtphase \
      --ifos H1 V1 \
      --relative-sensitivities 0.8 0.3 \
      --sample-size ${two_ifo_sample_size} \
      --batch-size ${batch_size} \
      --snr-ratio ${snr_ratio} \
      --seed ${seed} \
      --snr-reference ${snr_reference} \
      --output-file H1V1-stat.hdf \
      --timing-uncertainty 0.002 \
      --smoothing-sigma ${two_ifo_smoothing_sigma} \
      --snr-uncertainty ${snr_uncertainty} \
      --weight-threshold ${weight_threshold} \
      --bin-density ${two_ifo_bin_density} \
      --param-bin-dtype ${two_ifo_pb_dtype} \
      --verbose

# HLV
pycbc_multiifo_dtphase \
    --ifos L1 H1 V1  \
    --relative-sensitivities 1 0.8 0.3 \
    --sample-size ${three_ifo_sample_size} \
    --batch-size ${batch_size} \
    --snr-ratio ${snr_ratio} \
    --seed ${seed} \
    --snr-reference ${snr_reference} \
    --output-file L1H1V1-stat.hdf \
    --timing-uncertainty 0.002 \
    --smoothing-sigma ${three_ifo_smoothing_sigma} \
    --snr-uncertainty ${snr_uncertainty} \
    --weight-threshold ${weight_threshold} \
    --bin-density ${three_ifo_bin_density} \
    --param-bin-dtype ${three_ifo_pb_dtype} \
    --verbose
