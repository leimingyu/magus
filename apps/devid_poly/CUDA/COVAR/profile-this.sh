#!/bin/bash
#./covariance.exe $1

nvprof --metrics all --csv     --log-file metrics_poly_covariance.csv  ./covariance.exe 0 
# traces
nvprof --print-gpu-trace --csv --log-file  traces_poly_covariance.csv  ./covariance.exe 0 

mv metrics_*.csv ../../metrics/
mv traces_*.csv  ../../traces/




