#!/bin/bash
#./hotspot 512 2 2 ../data/hotspot/temp_512 ../data/hotspot/power_512 output.out $1

# metrics
nvprof --metrics all --csv     --log-file metrics_rodinia_hotspot.csv ./hotspot 512 2 2 ../data/hotspot/temp_512 ../data/hotspot/power_512 output.out 0 
# traces
nvprof --print-gpu-trace --csv --log-file  traces_rodinia_hotspot.csv ./hotspot 512 2 2 ../data/hotspot/temp_512 ../data/hotspot/power_512 output.out 0 

mv metrics_*.csv ../metrics/
mv traces_*.csv  ../traces/
