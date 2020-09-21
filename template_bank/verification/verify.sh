LIGO_USERNAME=${1}

if test x${LIGO_USERNAME} == "x" ; then
  echo "Error: user name not given."
  echo
  echo "Usage: ${0} ANALYSIS albert.einstein"
  echo
  echo "where albert.einstein is your LIGO.ORG username."
  exit 1
fi

source /cvmfs/oasis.opensciencegrid.org/ligo/sw/pycbc/x86_64_rhel_7/virtualenv/pycbc-v1.16.7/bin/activate
export LAL_DATA_PATH=/home/koustav.chandra/soft/hdf5_data/

WORKFLOW_NAME=HLV-SEOBNRv4ROM-bank
CONFIG_TAG='v1.15.6.0'
GPSSTART=1258642818
GPSEND=1258671618
CONFIG_DIR='/home/koustav.chandra/o3_devops/focusedimbhb_non_HM/bank_upto_500/restricted_q_space/q10t_cut/bank_verification'

ecp-cookie-init LIGO.ORG https://git.ligo.org/users/auth/shibboleth/callback ${LIGO_USERNAME}

pycbc_make_bank_verifier_workflow \
    --workflow-name ${WORKFLOW_NAME} --output-dir output \
    --config-files \
    ${CONFIG_DIR}/config.ini \
    ${CONFIG_DIR}/pointinjs.ini \
    --config-overrides workflow:start-time:${GPSSTART} workflow:end-time:${GPSEND} \
      'results_page:analysis-subtitle:"Verifying the template bank for 24 Nov O3 C01 H1L1V1 strain sensitivity. MM =0.99 q=10 70ms cut"' \
      results_page:output-path:"/home/${USER}/public_html/o3_dev_ops/bank_verification_600/q10tcut70" \
      workflow:file-retention-level:merged_triggers
