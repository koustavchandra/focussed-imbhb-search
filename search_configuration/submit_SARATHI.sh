CHUNKNUMBER=${1}

LIGO_USERNAME=${2}

if test x${LIGO_USERNAME} == "x" ; then
  echo "Error: user name not given."
  echo
  echo "Usage: ${0} ANALYSIS user.name"
  echo
  echo "where user.name is your LIGO.ORG username."
  exit 1
fi

WORKFLOW_NAME=o3
IMBH_CONFIG_TAG='v1.0.3'
CONFIG_TAG='v1.16.12.2'
DATA_TYPE='C01'
DATA_INI_NAME=data_O3_C01_clean.ini
DESCRIPTION='INITIAL'

GITLAB_URL_FULL_HL="https://git.ligo.org/ligo-cbc/pycbc-config/raw/${CONFIG_TAG}/O3C00/pipelineHL"
GITLAB_URL_FULL_HLV="https://git.ligo.org/ligo-cbc/pycbc-config/raw/${CONFIG_TAG}/O3C00/pipelineHLV"
GITLAB_URL_IMBHB_HLV="https://git.ligo.org/koustav.chandra/focussed-imbhb-search/-/raw/${IMBH_CONFIG_TAG}/search_configuration/"
GITLAB_URL_DATA_HLV="https://git.ligo.org/ligo-cbc/pycbc-config/raw/${CONFIG_TAG}/O3${DATA_TYPE}/pipelineHLV"
GITLAB_URL_BBH="https://git.ligo.org/ligo-cbc/pycbc-config/-/raw/master/O3C01/targetedBBHpipelineHLV/"

set -e 

source /cvmfs/oasis.opensciencegrid.org/ligo/sw/pycbc/x86_64_rhel_7/virtualenv/pycbc-v1.16.11/bin/activate
source /soft/intel/compilers_and_libraries_2018.0.128/linux/bin/compilervars.sh -arch intel64 -platform linux
export LIGO_DATAFIND_SERVER="ldr.gw.iucaa.in:80"
export PATH=/soft/intel/bin/:$PATH
export PATH=/soft/condor_mpi/bin:$PATH
export LAL_DATA_PATH=/home/koustav.chandra/soft/hdf5_data
export HDF5_USE_FILE_LOCKING=FALSE

ligo-proxy-init -p $LIGO_USERNAME
ecp-cookie-init LIGO.ORG https://git.ligo.org/users/auth/shibboleth/callback $LIGO_USERNAME

pycbc_create_offline_search_workflow \
  --workflow-name ${WORKFLOW_NAME} --output-dir a${CHUNKNUMBER}_${DESCRIPTION} \
  --config-files \
  ${GITLAB_URL_IMBHB_HLV}/analysis.ini \
  ${GITLAB_URL_FULL_HLV}/executables.ini \
  ${GITLAB_URL_IMBHB_HLV}/injections.ini \
  ${GITLAB_URL_IMBHB_HLV}/plotting.ini \
  ${GITLAB_URL_DATA_HLV}/${DATA_INI_NAME} \
  ${GITLAB_URL_FULL_HL}/gating.ini \
  ${GITLAB_URL_BBH}/gps_times_chunk${CHUNKNUMBER}.ini \
  --config-overrides 'results_page:analysis-subtitle:"O3 Targeted IMBHB Analysis BBH chunk-'${CHUNKNUMBER}', '${DATA_TYPE}' data"' \
       results_page:output-path:"/home/${USER}/public_html/o3/production/imbh/a${CHUNKNUMBER}_${DESCRIPTION}" \
       workflow:file-retention-level:all_triggers

cd a${CHUNKNUMBER}_${DESCRIPTION}
pycbc_submit_dax --accounting-group ligo.prod.o3.cbc.bbh.pycbcoffline --dax ${WORKFLOW_NAME}.dax --no-grid
