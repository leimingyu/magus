#!/bin/bash
#./gaussian -s 16 -d $1

# metrics
nvprof --metrics all --csv     --log-file metrics_rodinia_gaussian.csv  ./gaussian -s 16 -d 0 
# traces
nvprof --print-gpu-trace --csv --log-file  traces_rodinia_gaussian.csv	./gaussian -s 16 -d 0 

mv metrics_*.csv ../metrics/
mv traces_*.csv  ../traces/
