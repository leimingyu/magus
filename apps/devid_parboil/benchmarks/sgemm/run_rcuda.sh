#!/bin/bash

# run rcuda on mcx1
devid=$1
RCUDA_DEVICE_0=mcx1.coe.neu.edu:$devid ./sgemm  -i ../../datasets/sgemm/small/input/matrix1.txt,../../datasets/sgemm/small/input/matrix2.txt,../../datasets/sgemm/small/input/matrix2t.txt
