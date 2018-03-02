#!/bin/bash
./quasirandomGenerator $1

# metrics
nvprof --metrics all --csv     --log-file metrics_cudasdk_quasirandomGenerator.csv  ./quasirandomGenerator 0

# traces
nvprof --print-gpu-trace --csv --log-file  traces_cudasdk_quasirandomGenerator.csv  ./quasirandomGenerator 0

