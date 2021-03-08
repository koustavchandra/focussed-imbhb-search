#!/bin/bash
i=1
for DIR in `python list_analysis_directories.py`
do
    echo $DIR
    rsync -vzhe gsissh ${DIR}/allinj/*hdf ALLINJ/allinj_block${i}.hdf
    ((i=i+1))
done

results_directories="ALLINJ"

for dir in $results_directories
do
    chmod a+r $dir/*
done
