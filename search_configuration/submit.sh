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
CONFIG_TAG='v1.16.9.4'
DATA_TYPE='C01'
DATA_INI_NAME=data_O3_C01_clean.ini

GITLAB_URL_FULL_HL="https://git.ligo.org/ligo-cbc/pycbc-config/raw/${CONFIG_TAG}/O3C00/pipelineHL"
GITLAB_URL_FULL_HLV="https://git.ligo.org/ligo-cbc/pycbc-config/raw/${CONFIG_TAG}/O3C00/pipelineHLV"
GITLAB_URL_IMBHB_HLV="https://git.ligo.org/koustav.chandra/focussed-imbhb-search/-/raw/master/search_configuration/"
GITLAB_URL_DATA_HL="https://git.ligo.org/ligo-cbc/pycbc-config/raw/${CONFIG_TAG}/O3${DATA_TYPE}/pipelineHL"
GITLAB_URL_DATA_HLV="https://git.ligo.org/ligo-cbc/pycbc-config/raw/${CONFIG_TAG}/O3${DATA_TYPE}/pipelineHLV"
GITLAB_URL_BBH="https://git.ligo.org/ligo-cbc/pycbc-config/-/raw/master/O3C01/targetedBBHpipelineHLV/"

set -e 

source /cvmfs/oasis.opensciencegrid.org/ligo/sw/pycbc/x86_64_rhel_7/virtualenv/pycbc-v1.16.9/bin/activate
export LAL_DATA_PATH=/home/koustav.chandra/soft/hdf5_data
export HDF5_USE_FILE_LOCKING=FALSE

ligo-proxy-init -p $LIGO_USERNAME
ecp-cookie-init LIGO.ORG https://git.ligo.org/users/auth/shibboleth/callback $LIGO_USERNAME

pycbc_create_offline_search_workflow \
  --workflow-name ${WORKFLOW_NAME} --output-dir output \
  --config-files \
  ${GITLAB_URL_IMBHB_HLV}/analysis.ini \
  ${GITLAB_URL_FULL_HLV}/executables.ini \
  ${GITLAB_URL_IMBHB_HLV}/injections.ini \
  ${GITLAB_URL_IMBHB_HLV}/plotting.ini \
  ${GITLAB_URL_DATA_HLV}/${DATA_INI_NAME} \
  ${GITLAB_URL_FULL_HL}/gating.ini \
  ${GITLAB_URL_BBH}/gps_times_chunk${CHUNKNUMBER}.ini \
  --config-overrides 'results_page:analysis-subtitle:"O3 Targeted IMBHB Analysis BBH chunk-'${CHUNKNUMBER}', '${DATA_TYPE}' data with q = 10 Mt = 600"' \
       results_page:output-path:"/home/${USER}/public_html/o3/runs/focused-imbhb/${DATA_TYPE}/HLV/a${CHUNKNUMBER}" \
       workflow:file-retention-level:all_triggers