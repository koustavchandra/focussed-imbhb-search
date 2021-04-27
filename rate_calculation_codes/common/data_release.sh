source /cvmfs/oasis.opensciencegrid.org/ligo/sw/conda/etc/profile.d/conda.sh
conda activate igwn-py37
export NUMEXPR_MAX_THREADS=64

pycbc_dir=/home/koustav.chandra/O3/rate_calculation/nr_rate_inj/pycbc_inj/found_binwise/
cwb_dir=/home/koustav.chandra/O3/rate_calculation/nr_rate_inj/cwb_inj/found_binwise/
gstlal_dir=/home/koustav.chandra/O3/rate_calculation/nr_rate_inj/gstlal_inj/found_binwise/

rm -rf o3_imbhb_inj_info.h5

a=0

while [ $a -lt 5 ]
do
   echo $a

    python combine_pipelines.py --input-file bins_0_5_injections_v1.h5 --pycbc-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/pycbc_inj/found_binwise/pycbc_bin_number_${a}.csv --cwb-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/cwb_inj/found_binwise/cwb_bin_number_${a}.csv --gstlal-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/gstlal_inj/bin${a}.dat --massbin ${a}
   a=`expr $a + 1`
done

while [ $a -lt 10 ]
do
   echo $a

    python combine_pipelines.py --input-file bins_5_10_injections_v1.h5 --pycbc-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/pycbc_inj/found_binwise/pycbc_bin_number_${a}.csv --cwb-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/cwb_inj/found_binwise/cwb_bin_number_${a}.csv --gstlal-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/gstlal_inj/bin${a}.dat --massbin ${a}
   a=`expr $a + 1`
done

while [ $a -lt 15 ]
do
   echo $a

    python combine_pipelines.py --input-file bins_10_15_injections_v1.h5 --pycbc-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/pycbc_inj/found_binwise/pycbc_bin_number_${a}.csv --cwb-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/cwb_inj/found_binwise/cwb_bin_number_${a}.csv --gstlal-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/gstlal_inj/bin${a}.dat --massbin ${a}
   a=`expr $a + 1`
done

while [ $a -lt 20 ]
do
   echo $a

    python combine_pipelines.py --input-file bins_15_20_injections_v1.h5 --pycbc-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/pycbc_inj/found_binwise/pycbc_bin_number_${a}.csv --cwb-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/cwb_inj/found_binwise/cwb_bin_number_${a}.csv --gstlal-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/gstlal_inj/bin${a}.dat --massbin ${a}
   a=`expr $a + 1`
done

while [ $a -lt 25 ]
do
   echo $a

    python combine_pipelines.py --input-file bins_20_25_injections_v1.h5 --pycbc-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/pycbc_inj/found_binwise/pycbc_bin_number_${a}.csv --cwb-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/cwb_inj/found_binwise/cwb_bin_number_${a}.csv --gstlal-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/gstlal_inj/bin${a}.dat --massbin ${a}
   a=`expr $a + 1`
done

while [ $a -lt 30 ]
do
   echo $a

    python combine_pipelines.py --input-file bins_25_30_injections_v1.h5 --pycbc-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/pycbc_inj/found_binwise/pycbc_bin_number_${a}.csv --cwb-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/cwb_inj/found_binwise/cwb_bin_number_${a}.csv --gstlal-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/gstlal_inj/bin${a}.dat --massbin ${a}
   a=`expr $a + 1`
done

while [ $a -lt 35 ]
do
   echo $a

    python combine_pipelines.py --input-file bins_30_35_injections_v1.h5 --pycbc-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/pycbc_inj/found_binwise/pycbc_bin_number_${a}.csv --cwb-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/cwb_inj/found_binwise/cwb_bin_number_${a}.csv --gstlal-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/gstlal_inj/bin${a}.dat --massbin ${a}
   a=`expr $a + 1`
done

while [ $a -lt 40 ]
do
   echo $a

    python combine_pipelines.py --input-file bins_35_40_injections_v1.h5 --pycbc-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/pycbc_inj/found_binwise/pycbc_bin_number_${a}.csv --cwb-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/cwb_inj/found_binwise/cwb_bin_number_${a}.csv --gstlal-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/gstlal_inj/bin${a}.dat --massbin ${a}
   a=`expr $a + 1`
done

while [ $a -lt 46 ]
do
   echo $a

    python combine_pipelines.py --input-file bins_40_46_injections_v1.h5 --pycbc-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/pycbc_inj/found_binwise/pycbc_bin_number_${a}.csv --cwb-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/cwb_inj/found_binwise/cwb_bin_number_${a}.csv --gstlal-file /home/koustav.chandra/O3/rate_calculation/nr_rate_inj/gstlal_inj/bin${a}.dat --massbin ${a}
   a=`expr $a + 1`
done
