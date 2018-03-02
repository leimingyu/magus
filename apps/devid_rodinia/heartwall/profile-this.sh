#!/bin/bash
#./heartwall ../data/heartwall/test.avi 20 $1

# metrics
nvprof --metrics all --csv     --log-file metrics_rodinia_heartwall.csv  ./heartwall ../data/heartwall/test.avi 20 0 

# traces
nvprof --print-gpu-trace --csv --log-file  traces_rodinia_heartwall.csv  ./heartwall ../data/heartwall/test.avi 20 0 


mv metrics_*.csv ../metrics/
mv traces_*.csv  ../traces/
