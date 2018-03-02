#!/bin/bash
#./sssp ../../inputs/USA-road-d.FLA.gr

# metrics
nvprof --metrics all --csv     --log-file metrics_lonestar_sssp.csv ./sssp ../../inputs/USA-road-d.FLA.gr
# traces
nvprof --print-gpu-trace --csv --log-file  traces_lonestar_sssp.csv  ./sssp ../../inputs/USA-road-d.FLA.gr

mv metrics_*.csv ../../metrics/
mv traces_*.csv  ../../traces/
