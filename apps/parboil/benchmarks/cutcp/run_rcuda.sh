#!/bin/bash

devid=$1
RCUDA_DEVICE_0=mcx1.coe.neu.edu:$devid  ./cutcp -i ../../datasets/cutcp/small/input/watbox.sl40.pqr  -o out_small
