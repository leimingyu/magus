#!/bin/bash
devid=$1
RCUDA_DEVICE_0=mcx1.coe.neu.edu:$devid cuda/lud_cuda -s 256 -v
