# This script shows the location of the C01_sub60Hz HLV NR Injections run,
# and it is used by copy_from_original.sh

directories = [
    'koustav.chandra@ldas-pcdev1.gw.iucaa.in:/home/koustav.chandra/o3/imbh_nrinjs/a1_rerun/a1_rerun/',
    'koustav.chandra@ldas-pcdev1.gw.iucaa.in:/home/koustav.chandra/o3/imbh_nrinjs/a2_rerun/a2_rerun/',
    'koustav.chandra@ldas-grid.gw.iucaa.in:/home/koustav.chandra/o3/imbh_nrinjs/a3_rerun/a3_rerun/',
    'koustav.chandra@ldas-pcdev2.ligo-wa.caltech.edu:/home/koustav.chandra/O3/imbh_nrinjections/a4_INITIAL/',
    'koustav.chandra@ldas-grid.gw.iucaa.in:/home/kanchan.soni/IMBH_search/imbh-nrinjs/chunk5/a5_INITIAL/',
    'koustav.chandra@ldas-pcdev1.gw.iucaa.in:/home/kanchan.soni/IMBH_search/imbh-nrinjs/chunk6/a6_INITIAL/',
    'koustav.chandra@ldas-grid.gw.iucaa.in:/home/kanchan.soni/IMBH_search/chunk7_rerun/a7_INITIAL/',
    'koustav.chandra@ldas-pcdev2.ligo-wa.caltech.edu:/home/veronica.villa/o3/imbh_nrinjs/chunk8/a8_INITIAL/',
    'koustav.chandra@ldas-pcdev2.ligo-wa.caltech.edu:/home/veronica.villa/o3/imbh_nrinjs/chunk9/a9_INITIAL/']

print (' '.join(directories))
