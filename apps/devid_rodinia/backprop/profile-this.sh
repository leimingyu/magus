#!/bin/bash
#./backprop 65536 $1

# metrics
nvprof --metrics all --csv     --log-file metrics_rodinia_backprop.csv ./backprop 65536 0 
# traces
nvprof --print-gpu-trace --csv --log-file  traces_rodinia_backprop.csv ./backprop 65536 0 

mv metrics_*.csv ../metrics/
mv traces_*.csv  ../traces/


