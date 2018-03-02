#!/bin/bash
#./sgemm  -i ../../datasets/sgemm/small/input/matrix1.txt,../../datasets/sgemm/small/input/matrix2.txt,../../datasets/sgemm/small/input/matrix2t.txt -d $1

# metrics
nvprof --metrics all --csv     --log-file metrics_parboil_sgemm.csv ./sgemm  -i ../../datasets/sgemm/small/input/matrix1.txt,../../datasets/sgemm/small/input/matrix2.txt,../../datasets/sgemm/small/input/matrix2t.txt -d 0 
# traces
nvprof --print-gpu-trace --csv --log-file  traces_parboil_sgemm.csv ./sgemm  -i ../../datasets/sgemm/small/input/matrix1.txt,../../datasets/sgemm/small/input/matrix2.txt,../../datasets/sgemm/small/input/matrix2t.txt -d 0 

mv metrics_*.csv ../../metrics/
mv traces_*.csv  ../../traces/
