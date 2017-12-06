#!/bin/bash
devid=$1
RCUDA_DEVICE_0=mcx1.coe.neu.edu:$devid  ./stencil -i ../../datasets/stencil/small/input/128x128x32.bin 128 128 32 100
