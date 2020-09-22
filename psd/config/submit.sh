ligo-proxy-init koustav.chandra

source /cvmfs/oasis.opensciencegrid.org/ligo/sw/pycbc/x86_64_rhel_7/virtualenv/pycbc-v1.16.4/bin/activate
WORKFLOW_NAME=psd-estimation-O3-HLV-Nov24
GPSSTART=1258642818 # 24th Nov 2019 15:00: 00 UTC
GPSEND=1258671618 # 24th Nov 2019 23:00:00 UTC
CONFIG_URL='/home/koustav.chandra/o3_dev_ops/psds'

ecp-cookie-init LIGO.ORG https://git.ligo.org/users/auth/shibboleth/callback koustav.chandra


pycbc_make_psd_estimation_workflow \
    --workflow-name ${WORKFLOW_NAME} \
    --output-dir output \
    --config-files \
        ${CONFIG_URL}/psd_estimation.ini \
        ${CONFIG_URL}/data_O3_C01.ini \
        ${CONFIG_URL}/gps_times.ini \
    --config-overrides workflow:start-time:${GPSSTART} workflow:end-time:${GPSEND} \
      results_page:output-path:"/home/${USER}/public_html/o3/psds/hlv/c01/" \


