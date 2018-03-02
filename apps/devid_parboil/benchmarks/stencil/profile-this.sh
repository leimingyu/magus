#!/bin/bash
#./stencil -i ../../datasets/stencil/small/input/128x128x32.bin 128 128 32 100 -d $1

# metrics
nvprof --metrics all --csv     --log-file metrics_parboil_stencil.csv  ./stencil -i ../../datasets/stencil/small/input/128x128x32.bin 128 128 32 100 -d 0 
# traces
nvprof --print-gpu-trace --csv --log-file  traces_parboil_stencil.csv  ./stencil -i ../../datasets/stencil/small/input/128x128x32.bin 128 128 32 100 -d 0


mv metrics_*.csv ../../metrics/
mv traces_*.csv  ../../traces/
