source /cvmfs/oasis.opensciencegrid.org/ligo/sw/conda/etc/profile.d/conda.sh
conda activate igwn-py37
export NUMEXPR_MAX_THREADS=32

pycbc_dir=/home/koustav.chandra/O3/rate_calculation/nr_rate_inj/pycbc_inj/found_binwise/
cwb_dir=/home/koustav.chandra/O3/rate_calculation/nr_rate_inj/cwb_inj/found_binwise/
gstlal_dir=/home/koustav.chandra/O3/rate_calculation/nr_rate_inj/gstlal_inj/found_binwise/
output_dir=/nfshome/store01/users/koustav.chandra/O3/rate_calculation/nr_rate_inj/common_inj/found_combined/

if [[ -d "$output_dir" ]]
then 
    echo "$output_dir exists on your filesystem."
else
    echo "Making directory $output_dir"
    mkdir $output_dir
fi

a=0

while [ $a -lt 46 ]
do
   echo $a
   python combine_or_inj.py --pycbc-bin-file ${pycbc_dir}/pycbc_bin_number_${a}.csv  --cwb-bin-file ${cwb_dir}/cwb_bin_number_${a}.csv --gstlal-bin-file ${gstlal_dir}/gstlal_bin_${a}.csv --output-file ${output_dir}/combined_${a}.csv
   a=`expr $a + 1`
done

