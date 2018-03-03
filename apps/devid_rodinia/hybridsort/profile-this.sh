#!/bin/bash
#./hybridsort r $1

# metrics
nvprof --metrics all --csv     --log-file metrics_rodinia_hybridsort.csv  ./hybridsort r 0
# traces
nvprof --print-gpu-trace --csv --log-file  traces_rodinia_hybridsort.csv  ./hybridsort r 0

mv metrics_*.csv ../metrics/
mv traces_*.csv  ../traces/
