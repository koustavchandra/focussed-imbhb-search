source /cvmfs/oasis.opensciencegrid.org/ligo/sw/conda/etc/profile.d/conda.sh
conda activate igwn-py37
export NUMEXPR_MAX_THREADS=32
output_dir=/nfshome/store01/users/koustav.chandra/O3/rate_calculation/nr_rate_inj/pycbc_inj/binwise

python pycbc_extract_binwise.py --mtotal 120 --mratio 1 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_120_q_1_chieff_0_chip_0.csv --mass-bin 0
python pycbc_extract_binwise.py --mtotal 120 --mratio 2 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_120_q_2_chieff_0_chip_0.csv --mass-bin 1
python pycbc_extract_binwise.py --mtotal 120 --mratio 4 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_120_q_4_chieff_0_chip_0.csv --mass-bin 2
python pycbc_extract_binwise.py --mtotal 120 --mratio 5 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_120_q_5_chieff_0_chip_0.csv --mass-bin 3
python pycbc_extract_binwise.py --mtotal 120 --mratio 7 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_120_q_7_chieff_0_chip_0.csv --mass-bin 4
python pycbc_extract_binwise.py --mtotal 120 --mratio 10 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_120_q_10_chieff_0_chip_0.csv --mass-bin 5 

python pycbc_extract_binwise.py --mtotal 150 --mratio 2 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_150_q_2_chieff_0_chip_0.csv --mass-bin 6

python pycbc_extract_binwise.py --mtotal 200 --mratio 1 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_200_q_1_chieff_0_chip_0.csv --mass-bin 7
python pycbc_extract_binwise.py --mtotal 200 --mratio 2 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_200_q_2_chieff_0_chip_0.csv --mass-bin 8
python pycbc_extract_binwise.py --mtotal 200 --mratio 4 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_200_q_4_chieff_0_chip_0.csv --mass-bin 9
python pycbc_extract_binwise.py --mtotal 200 --mratio 7 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_200_q_7_chieff_0_chip_0.csv --mass-bin 10

python pycbc_extract_binwise.py --mtotal 220 --mratio 10 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_220_q_10_chieff_0_chip_0.csv --mass-bin 11

python pycbc_extract_binwise.py --mtotal 250 --mratio 4 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_250_q_4_chieff_0_chip_0.csv --mass-bin 12

python pycbc_extract_binwise.py --mtotal 300 --mratio 2 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_300_q_2_chieff_0_chip_0.csv --mass-bin 13

python pycbc_extract_binwise.py --mtotal 350 --mratio 6 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_350_q_6_chieff_0_chip_0.csv --mass-bin 14

python pycbc_extract_binwise.py --mtotal 400 --mratio 1 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_400_q_1_chieff_0_chip_0.csv --mass-bin 15
python pycbc_extract_binwise.py --mtotal 400 --mratio 2 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_400_q_2_chieff_0_chip_0.csv --mass-bin 16
python pycbc_extract_binwise.py --mtotal 400 --mratio 3 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_400_q_3_chieff_0_chip_0.csv --mass-bin 17
python pycbc_extract_binwise.py --mtotal 400 --mratio 4 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_400_q_4_chieff_0_chip_0.csv --mass-bin 18
python pycbc_extract_binwise.py --mtotal 400 --mratio 7 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_400_q_7_chieff_0_chip_0.csv --mass-bin 19

python pycbc_extract_binwise.py --mtotal 440 --mratio 10 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_440_q_10_chieff_0_chip_0.csv --mass-bin 20

python pycbc_extract_binwise.py --mtotal 500 --mratio 1.5 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_500_q_15_chieff_0_chip_0.csv --mass-bin 21

python pycbc_extract_binwise.py --mtotal 600 --mratio 1 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_600_q_1_chieff_0_chip_0.csv --mass-bin 22
python pycbc_extract_binwise.py --mtotal 600 --mratio 2 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_600_q_2_chieff_0_chip_0.csv --mass-bin 23

python pycbc_extract_binwise.py --mtotal 800 --mratio 1 --chieff 0. --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_800_q_1_chieff_0_chip_0.csv --mass-bin 24

python pycbc_extract_binwise.py --mtotal 120 --mratio 1 --chieff 0.8 --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_120_q_1_chieff_08_chip_0.csv --mass-bin 25
python pycbc_extract_binwise.py --mtotal 200 --mratio 1 --chieff 0.8 --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_200_q_1_chieff_08_chip_0.csv --mass-bin 26
python pycbc_extract_binwise.py --mtotal 400 --mratio 1 --chieff 0.8 --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_400_q_1_chieff_08_chip_0.csv --mass-bin 27
python pycbc_extract_binwise.py --mtotal 600 --mratio 1 --chieff 0.8 --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_600_q_1_chieff_08_chip_0.csv --mass-bin 28
python pycbc_extract_binwise.py --mtotal 800 --mratio 1 --chieff 0.8 --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_800_q_1_chieff_08_chip_0.csv --mass-bin 29

python pycbc_extract_binwise.py --mtotal 120 --mratio 1 --chieff -0.8 --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_120_q_1_chieff_minus08_chip_0.csv --mass-bin 30
python pycbc_extract_binwise.py --mtotal 200 --mratio 1 --chieff -0.8 --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_200_q_1_chieff_minus08_chip_0.csv --mass-bin 31
python pycbc_extract_binwise.py --mtotal 400 --mratio 1 --chieff -0.8 --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_400_q_1_chieff_minus08_chip_0.csv --mass-bin 32
python pycbc_extract_binwise.py --mtotal 600 --mratio 1 --chieff -0.8 --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_600_q_1_chieff_minus08_chip_0.csv --mass-bin 33
python pycbc_extract_binwise.py --mtotal 800 --mratio 1 --chieff -0.8 --chip 0. --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_800_q_1_chieff_minus08_chip_0.csv --mass-bin 34

python pycbc_extract_binwise.py --mtotal 200 --mratio 1 --chieff 0.51 --chip 0.42 --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_200_q_1_chieff_051_chip_042.csv --mass-bin 35
python pycbc_extract_binwise.py --mtotal 200 --mratio 2 --chieff 0.14 --chip 0.42 --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_200_q_2_chieff_014_chip_042.csv --mass-bin 36
python pycbc_extract_binwise.py --mtotal 200 --mratio 4 --chieff 0.26 --chip 0.42 --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_200_q_4_chieff_026_chip_042.csv --mass-bin 37
python pycbc_extract_binwise.py --mtotal 200 --mratio 7 --chieff 0.32 --chip 0.42 --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_200_q_7_chieff_032_chip_042.csv --mass-bin 38

python pycbc_extract_binwise.py --mtotal 400 --mratio 1 --chieff 0.51 --chip 0.42 --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_400_q_1_chieff_051_chip_042.csv --mass-bin 39
python pycbc_extract_binwise.py --mtotal 400 --mratio 2 --chieff 0.14 --chip 0.42 --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_400_q_2_chieff_014_chip_042.csv --mass-bin 40
python pycbc_extract_binwise.py --mtotal 400 --mratio 4 --chieff 0.26 --chip 0.42 --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_400_q_4_chieff_026_chip_042.csv --mass-bin 41
python pycbc_extract_binwise.py --mtotal 400 --mratio 7 --chieff 0.32 --chip 0.42 --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_400_q_7_chieff_032_chip_042.csv --mass-bin 42

python pycbc_extract_binwise.py --mtotal 600 --mratio 1 --chieff 0.51 --chip 0.42 --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_600_q_1_chieff_051_chip_042.csv --mass-bin 43
python pycbc_extract_binwise.py --mtotal 600 --mratio 2 --chieff 0.14 --chip 0.42 --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_600_q_2_chieff_014_chip_042.csv --mass-bin 44

python pycbc_extract_binwise.py --mtotal 800 --mratio 1 --chieff 0.51 --chip 0.42 --ifar 2.94 --input-file allinj.csv --output-file ${output_dir}/mtotal_800_q_1_chieff_051_chip_042.csv --mass-bin 45
