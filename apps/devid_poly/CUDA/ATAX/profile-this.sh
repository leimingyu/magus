#!/bin/bash
#./atax.exe $1

# metrics
nvprof --metrics all --csv     --log-file metrics_poly_atax.csv ./atax.exe 0 
# traces
nvprof --print-gpu-trace --csv --log-file  traces_poly_atax.csv ./atax.exe 0

mv metrics_*.csv ../../metrics/
mv traces_*.csv  ../../traces/
