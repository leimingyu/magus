#!/bin/bash

#LD_LIBRARY_PATH="/usr/local/cuda/lib64"
#export LD_LIBRARY_PATH

appDir=$1
appExe=$2
#targetMetric=$3

#echo $appDir
#echo $appExe
#echo $targetMetric

out_metrics=$appExe"_metrics.csv"
#echo $out_metrics

#cd $appDir && \
#make clean && \
#make && \
#nvprof --metrics $targetMetric  --csv --log-file $out_metrics $appExe

cd $appDir && nvprof --metrics all --csv --log-file $out_metrics $appExe

