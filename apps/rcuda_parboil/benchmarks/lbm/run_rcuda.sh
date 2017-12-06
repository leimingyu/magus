#!/bin/bash

devid=$1
RCUDA_DEVICE_0=mcx1.coe.neu.edu:$devid ./lbm 1 -i ../../datasets/lbm/short/input/120_120_150_ldc.of   -o out
