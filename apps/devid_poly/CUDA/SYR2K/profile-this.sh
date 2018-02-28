#!/bin/bash
#./syr2k.exe $1


# metrics
nvprof --metrics all --csv     --log-file metrics_poly_syr2k.csv ./syr2k.exe 0
# traces
nvprof --print-gpu-trace --csv --log-file  traces_poly_syr2k.csv ./syr2k.exe 0

mv metrics_*.csv ../../metrics/
mv traces_*.csv  ../../traces/


