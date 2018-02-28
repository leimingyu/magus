#!/bin/bash
#./fdtd2d.exe $1

# metrics
nvprof --metrics all --csv     --log-file metrics_poly_fdtd2d.csv  ./fdtd2d.exe 0 
# traces
nvprof --print-gpu-trace --csv --log-file  traces_poly_fdtd2d.csv  ./fdtd2d.exe 0 

mv metrics_*.csv ../../metrics/
mv traces_*.csv  ../../traces/
