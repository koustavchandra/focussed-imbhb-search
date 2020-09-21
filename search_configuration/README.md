# O3 C00 data 3-ifo Focused IMBHB Pipeline Configuration Files #

This directory contains the necessary PyCBC workflow configuration files to
run the ``pycbc_make_coinc_search_workflow`` generator on ER14 or O3 data
to run the focused IMBHB pipeline.

## Analysis Configuration ##

The files

 * analysis.ini
 * plotting.ini
The other files like are same as HL search
 * executables.ini
 * injections.ini

are the primary workflow configuration files.  In addition files named eg data.ini, gating.ini, gps_times.ini are used to give specific information about the data to be run on and data quality. For the BBH focused search both plotting.ini and executables.ini are taken from the full hyperbank search, only analysis.ini and injections_minimal.ini are unique here.

The bank being used is the IMBHB bank with <img src="https://latex.codecogs.com/gif.latex?100&space;M_\odot&space;\leq&space;M_T&space;\leq&space;500&space;M_\odot" title="100 M_\odot \leq M_T \leq 500 M_\odot" />. If you wish to run with <img src="https://latex.codecogs.com/gif.latex?100&space;M_\odot&space;\leq&space;M_T&space;\leq&space;600&space;M_\odot" title="100 M_\odot \leq M_T \leq 600 M_\odot" /> assign the 
```
tmpltbank-pregenerated-bank=https://git.ligo.org/koustav.chandra/pycbc-config/-/raw/focusedimbhb/O3C00/focusedIMBHBpipeline/bank/flow15Hz_upto_600/q10duration70/H1L1V1-H5ADD_CYCLE12_FINAL-1258642818-28800.h5
``` 
in the `analysis.ini`

To create the workflow for C01_sub60Hz data run `bash submit.sh 1 user.name` where 1 is the BBH Chunk number. Also change the chunk number as per choice of time. If you wish to create the workflow for C01 run `bash submit.sh C01 user.name`. When the above command completes successfully, submit the workflow by:
```
cd output
pycbc_submit_dax --accounting-group ligo.dev.o3.cbc.bbh.pycbcoffline --dax o3.dax --no-grid
```

For further details including run diagnosis and debugging see [this link](https://pycbc.org/pycbc/latest/html/workflow/pycbc_make_coinc_search_workflow.html#monitor-and-debug-the-workflow-detailed-pegasus-documentation).
