LIGO_USERNAME=${1}

if test x${LIGO_USERNAME} == "x" ; then
  echo "Error: user name not given."
  echo
  echo "Usage: ${0} ANALYSIS albert.einstein"
  echo
  echo "where albert.einstein is your LIGO.ORG username."
  exit 1
fi

ecp-cookie-init LIGO.ORG https://git.ligo.org/users/auth/shibboleth/callback ${LIGO_USERNAME}

source /cvmfs/oasis.opensciencegrid.org/ligo/sw/pycbc/x86_64_rhel_7/virtualenv/pycbc-v1.16.6/bin/activate
export LAL_DATA_PATH=/home/koustav.chandra/soft/hdf5_data/

GPSSTART=1258642818 
GPSEND=1258671618 


WORKFLOW_NAME=HLV-SEOBNRv4ROM-bank
CONFIG_URL="/home/koustav.chandra/o3_devops/focusedimbhb_non_HM/bank_upto_500/restricted_q_space/q10t_cut"

pycbc_make_sbank_workflow \
    --workflow-name ${WORKFLOW_NAME} --output-dir output \
    --config-files ${CONFIG_URL}/tmpltbank.ini \
    --config-overrides workflow:start-time:${GPSSTART} workflow:end-time:${GPSEND}
