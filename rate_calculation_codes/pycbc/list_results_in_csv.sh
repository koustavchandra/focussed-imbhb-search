source /cvmfs/oasis.opensciencegrid.org/ligo/sw/conda/etc/profile.d/conda.sh
conda activate igwn-py37
export NUMEXPR_MAX_THREADS=64
export HDF5_USE_FILE_LOCKING=FALSE
dir=/home/koustav.chandra/O3/rate_calculation/nr_rate_inj/pycbc_inj/ALLINJ

nohup python ./pycbc_found_injections.py --injection-file ${dir}/allinj_block1.hdf ${dir}/allinj_block2.hdf  ${dir}/allinj_block3.hdf ${dir}/allinj_block4.hdf  ${dir}/allinj_block5.hdf ${dir}/allinj_block6.hdf ${dir}/allinj_block7.hdf ${dir}/allinj_block8.hdf ${dir}/allinj_block9.hdf --output-file found_inj.csv > hdf2csv.out