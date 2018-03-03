#!/bin/bash
#./sc_gpu 10 20 256 65536 65536 1000 none output.txt 1 $1



# metrics
nvprof --metrics all --csv     --log-file metrics_rodinia_sc.csv  ./sc_gpu 10 20 256 65536 65536 1000 none output.txt 1 0 
# traces
nvprof --print-gpu-trace --csv --log-file  traces_rodinia_sc.csv  ./sc_gpu 10 20 256 65536 65536 1000 none output.txt 1 0

mv metrics_*.csv ../metrics/
mv traces_*.csv  ../traces/

