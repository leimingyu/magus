#!/bin/bash
#cuda/lud_cuda -s 256 -v -d $1


# metrics
nvprof --metrics all --csv     --log-file metrics_rodinia_lud.csv  cuda/lud_cuda -s 256 -v -d 0 
# traces
nvprof --print-gpu-trace --csv --log-file  traces_rodinia_lud.csv  cuda/lud_cuda -s 256 -v -d 0 

mv metrics_*.csv ../metrics/
mv traces_*.csv  ../traces/


