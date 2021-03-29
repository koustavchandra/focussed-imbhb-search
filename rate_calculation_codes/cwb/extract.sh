source /cvmfs/oasis.opensciencegrid.org/ligo/sw/conda/etc/profile.d/conda.sh
conda activate igwn-py37
export NUMEXPR_MAX_THREADS=32
a=0
dir=/home/koustav.chandra/O3/rate_calculation/nr_rate_inj/cwb_inj/found_binwise
while [ $a -lt 46 ]
do
   echo $a
   python cwb_found_binwise.py --input-file O3_K99_IMBH_inj.csv --bin-number $a --output-file ${dir}/cwb_bin_number_${a}.csv
   a=`expr $a + 1`
done

