source /cvmfs/oasis.opensciencegrid.org/ligo/sw/conda/etc/profile.d/conda.sh
conda activate igwn-py37
export NUMEXPR_MAX_THREADS=32
a=0
dir=/home/koustav.chandra/O3/rate_calculation/nr_rate_inj/gstlal_inj
while [ $a -lt 46 ]
do
   echo $a
   python gstlal_found_binwise.py --input-file bin${a}.dat --output-dir ${dir}/found_binwise
   a=`expr $a + 1`
done

