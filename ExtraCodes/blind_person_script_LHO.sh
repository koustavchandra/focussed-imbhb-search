source /cvmfs/oasis.opensciencegrid.org/ligo/sw/conda/etc/profile.d/conda.sh
conda activate igwn-py37

dir_4='/home/koustav.chandra/O3/productions/imbh/a4_initial/a4_INITIAL/full_data/'
python /home/koustav.chandra/O3/pycbc_page_background.py \
--statmap-file ${dir_4}H1L1-EXCLUDE_ZEROLAG_FULL_DATA_2DET-1246824215-3850078.hdf \
--single-trigger-files H1:${dir_4}/H1-HDF_TRIGGER_MERGE_FULL_DATA-1246824215-3850078.hdf L1:${dir_4}/L1-HDF_TRIGGER_MERGE_FULL_DATA-1246824215-3850078.hdf \
--output-file 'H1L1-EXC_IFAR_BLOCK4.csv'

echo "H1L1-EXC_IFAR_BLOCK4.csv generated"

dir_8='/home/veronica.villa/o3/imbh_search/chunk8/a8_INITIAL/full_data/'
python /home/koustav.chandra/O3/pycbc_page_background.py \
--statmap-file ${dir_8}H1L1-EXCLUDE_ZEROLAG_FULL_DATA_2DET-1262946323-3516749.hdf \
--single-trigger-files H1:${dir_8}/H1-HDF_TRIGGER_MERGE_FULL_DATA-1262946323-3516749.hdf L1:${dir_8}/L1-HDF_TRIGGER_MERGE_FULL_DATA-1262946323-3516749.hdf \
--output-file 'H1L1-EXC_IFAR_BLOCK8.csv'

echo "H1L1-EXC_IFAR_BLOCK8.csv generated"

dir_9='/home/veronica.villa/o3/imbh_search/chunk9/a9_INITIAL/full_data/'
python /home/koustav.chandra/O3/pycbc_page_background.py \
--statmap-file ${dir_9}H1L1-EXCLUDE_ZEROLAG_FULL_DATA_2DET-1266462896-3098746.hdf \
--single-trigger-files H1:${dir_9}/H1-HDF_TRIGGER_MERGE_FULL_DATA-1266462896-3098746.hdf L1:${dir_9}/L1-HDF_TRIGGER_MERGE_FULL_DATA-1266462896-3098746.hdf \
--output-file 'H1L1-EXC_IFAR_BLOCK9.csv'

echo "H1L1-EXC_IFAR_BLOCK9.csv generated"
