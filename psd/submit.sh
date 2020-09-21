LIGO_USERNAME=${1}

if test x${LIGO_USERNAME} == "x" ; then
  echo "Error: user name not given."
  echo
  echo "Usage: ${0} ANALYSIS albert.einstein"
  echo
  echo "where albert.einstein is your LIGO.ORG username."
  exit 1
fi

ligo-proxy-init -p $LIGO_USERNAME

source /cvmfs/oasis.opensciencegrid.org/ligo/sw/pycbc/x86_64_rhel_7/virtualenv/pycbc-v1.16.4/bin/activate
WORKFLOW_NAME=psd-estimation-O3-HLV-Nov24
GPSSTART=1258642818 # 24th Nov 2019 15:00: 00 UTC
GPSEND=1258671618 # 24th Nov 2019 23:00:00 UTC
CONFIG_URL='https://git.ligo.org/koustav.chandra/pycbc-config/-/raw/focusedimbhb/O3C00/focusedIMBHBpipeline/psds/config/'

ecp-cookie-init LIGO.ORG https://git.ligo.org/users/auth/shibboleth/callback $LIGO_USERNAME


pycbc_make_psd_estimation_workflow \
    --workflow-name ${WORKFLOW_NAME} \
    --output-dir output \
    --config-files \
        ${CONFIG_URL}/psd_estimation.ini \
        ${CONFIG_URL}/data_O3_C01.ini \
        ${CONFIG_URL}/gps_times.ini \
    --config-overrides workflow:start-time:${GPSSTART} workflow:end-time:${GPSEND} \
      results_page:output-path:"/home/${USER}/public_html/o3/psds/hlv/c01/" \