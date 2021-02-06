source /cvmfs/oasis.opensciencegrid.org/ligo/sw/conda/etc/profile.d/conda.sh
conda activate igwn-py37
export NUMEXPR_MAX_THREADS=32
a=0

while [ $a -lt 46 ]
do
   echo $a
   python extract_binwise.py --input-file O3_K99_IMBH_NR_inj.csv --bin-number $a --output-file bin_number_${a}.csv
   a=`expr $a + 1`
done


