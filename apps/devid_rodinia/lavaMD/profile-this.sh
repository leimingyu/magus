#!/bin/bash
#./lavaMD -boxes1d 10 -d $1

# metrics
nvprof --metrics all --csv     --log-file metrics_rodinia_lavaMD.csv ./lavaMD -boxes1d 10 -d 0 
# traces
nvprof --print-gpu-trace --csv --log-file  traces_rodinia_lavaMD.csv ./lavaMD -boxes1d 10 -d 0 

mv metrics_*.csv ../metrics/
mv traces_*.csv  ../traces/

