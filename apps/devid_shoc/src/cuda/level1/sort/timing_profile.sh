#!/bin/bash


# metrics
# featAll

ts=$(date +%s%N)

nvprof --metrics all --csv     --log-file metrics_shoc_lev1sort.csv ./Sort -d 0

runtime_ms=$((($(date +%s%N) - $ts)/1000000))

echo -e "\n$appname:$runtime_ms" 
