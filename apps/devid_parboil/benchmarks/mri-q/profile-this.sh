#!/bin/bash
#./mri-q -i ../../datasets/mri-q/small/input/32_32_32_dataset.bin -d $1

# metrics
nvprof --metrics all --csv     --log-file metrics_parboil_mriq.csv  ./mri-q -i ../../datasets/mri-q/small/input/32_32_32_dataset.bin -d 0
# traces
nvprof --print-gpu-trace --csv --log-file  traces_parboil_mriq.csv ./mri-q -i ../../datasets/mri-q/small/input/32_32_32_dataset.bin -d 0


mv metrics_*.csv ../../metrics/
mv traces_*.csv  ../../traces/

