#!/bin/bash
#./needle 2048 10 $1

# metrics
nvprof --metrics all --csv     --log-file metrics_rodinia_needle.csv ./needle 2048 10 0 
# traces
nvprof --print-gpu-trace --csv --log-file  traces_rodinia_needle.csv ./needle 2048 10 0

mv metrics_*.csv ../metrics/
mv traces_*.csv  ../traces/
