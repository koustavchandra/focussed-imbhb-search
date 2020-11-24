source /cvmfs/oasis.opensciencegrid.org/ligo/sw/conda/etc/profile.d/conda.sh
conda activate igwn-py37

dir_1='/home/koustav.chandra/o3/productions/imbh/a1_initial/a1_INITIAL/full_data/'
python /home/koustav.chandra/o3/pycbc_page_background.py \
--statmap-file ${dir_1}H1L1-EXCLUDE_ZEROLAG_FULL_DATA_2DET-1238165866-2845260.hdf \
--single-trigger-files H1:${dir_1}/H1-HDF_TRIGGER_MERGE_FULL_DATA-1238165866-2845260.hdf L1:${dir_1}/L1-HDF_TRIGGER_MERGE_FULL_DATA-1238165866-2845260.hdf \
--output-file 'H1L1-EXC_IFAR_BLOCK1.csv'

echo "H1L1-EXC_IFAR_BLOCK1.csv generated"

dir_2='/home/koustav.chandra/o3/productions/imbh/a2_initial/a2_INITIAL/full_data/'
python /home/koustav.chandra/o3/pycbc_page_background.py \
--statmap-file ${dir_2}H1L1-EXCLUDE_ZEROLAG_FULL_DATA_2DET-1241010950-2775964.hdf \
--single-trigger-files H1:${dir_2}/H1-HDF_TRIGGER_MERGE_FULL_DATA-1241010950-2775964.hdf L1:${dir_2}/L1-HDF_TRIGGER_MERGE_FULL_DATA-1241010950-2775964.hdf \
--output-file 'H1L1-EXC_IFAR_BLOCK2.csv'

echo "H1L1-EXC_IFAR_BLOCK2.csv generated"

dir_3='/home/koustav.chandra/o3/productions/imbh/a3_initial/a3_INITIAL/full_data/'
python /home/koustav.chandra/o3/pycbc_page_background.py \
--statmap-file ${dir_3}H1L1-EXCLUDE_ZEROLAG_FULL_DATA_2DET-1243786738-3037653.hdf \
--single-trigger-files H1:${dir_3}/H1-HDF_TRIGGER_MERGE_FULL_DATA-1243786738-3037653.hdf L1:${dir_3}/L1-HDF_TRIGGER_MERGE_FULL_DATA-1243786738-3037653.hdf \
--output-file 'H1L1-EXC_IFAR_BLOCK3.csv'

echo "H1L1-EXC_IFAR_BLOCK3.csv generated"

dir_5='/home/kanchan.soni/IMBH_search/chunk5/a5_INITIAL/full_data/'
python /home/koustav.chandra/o3/pycbc_page_background.py \
--statmap-file ${dir_5}H1L1-EXCLUDE_ZEROLAG_FULL_DATA_2DET-1250674117-3335525.hdf \
--single-trigger-files H1:${dir_5}/H1-HDF_TRIGGER_MERGE_FULL_DATA-1250674117-3335525.hdf L1:${dir_5}/L1-HDF_TRIGGER_MERGE_FULL_DATA-1250674117-3335525.hdf \
--output-file 'H1L1-EXC_IFAR_BLOCK5.csv'

echo "H1L1-EXC_IFAR_BLOCK5.csv generated"


dir_6='/home/kanchan.soni/IMBH_search/chunk6/a6_INITIAL/full_data/'
python /home/koustav.chandra/o3/pycbc_page_background.py \
--statmap-file ${dir_6}H1L1-EXCLUDE_ZEROLAG_FULL_DATA_2DET-1256655490-2767934.hdf \
--single-trigger-files H1:${dir_6}/H1-HDF_TRIGGER_MERGE_FULL_DATA-1256655490-2767934.hdf L1:${dir_6}/L1-HDF_TRIGGER_MERGE_FULL_DATA-1256655490-2767934.hdf \
--output-file 'H1L1-EXC_IFAR_BLOCK6.csv'

echo "H1L1-EXC_IFAR_BLOCK6.csv generated"

dir_7='/home/kanchan.soni/IMBH_search/chunk7/a7_INITIAL/full_data/'
python /home/koustav.chandra/o3/pycbc_page_background.py \
--statmap-file ${dir_7}H1L1-EXCLUDE_ZEROLAG_FULL_DATA_2DET-1259423248-3523251.hdf \
--single-trigger-files H1:${dir_7}/H1-HDF_TRIGGER_MERGE_FULL_DATA-1259423248-3523251.hdf L1:${dir_7}/L1-HDF_TRIGGER_MERGE_FULL_DATA-1259423248-3523251.hdf \
--output-file 'H1L1-EXC_IFAR_BLOCK7.csv'

echo "H1L1-EXC_IFAR_BLOCK7.csv generated"