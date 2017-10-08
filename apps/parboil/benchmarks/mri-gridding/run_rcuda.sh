#!/bin/bash
devid=$1
RCUDA_DEVICE_0=mcx1.coe.neu.edu:$devid  ./mri-gridding  -i ../../datasets/mri-gridding/small/input/small.uks -o out.log
