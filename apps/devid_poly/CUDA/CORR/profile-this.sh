#!/bin/bash
#./correlation.exe $1

# metrics
nvprof --metrics all --csv     --log-file metrics_poly_correlation.csv ./correlation.exe 0 
# traces
nvprof --print-gpu-trace --csv --log-file  traces_poly_correlation.csv ./correlation.exe 0 

mv metrics_*.csv ../../metrics/
mv traces_*.csv  ../../traces/


