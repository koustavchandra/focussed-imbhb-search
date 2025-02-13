# O3 C01_sub60Hz data 3-ifo Focused IMBHB Pipeline Configuration Files #

This directory contains the necessary PyCBC workflow configuration files to
run the ``pycbc_make_coinc_search_workflow`` generator on ER14 or O3 data
to run the focused IMBHB pipeline.

## Analysis Configuration ##

The files

 * analysis.ini
 * plotting.ini
 * injections.ini

are the primary workflow configuration files.  Other ini files are the same as used in Focussed BBH search.

The bank being used for the runs is the IMBHB bank with <img src="https://latex.codecogs.com/gif.latex?100&space;M_\odot&space;\leq&space;M_T&space;\leq&space;600&space;M_\odot" title="100 M_\odot \leq M_T \leq 600 M_\odot" />  and duration cut of 70 ms starting from 15 Hz. 

To create the workflow for C01_sub60Hz data run `bash submit.sh 1 user.name` where 1 is the BBH Chunk number. Change the chunk number as per choice of time. 

For further details including run diagnosis and debugging see [this link](https://pycbc.org/pycbc/latest/html/workflow/pycbc_make_coinc_search_workflow.html#monitor-and-debug-the-workflow-detailed-pegasus-documentation).
