#!/bin/bash
devid=$1
RCUDA_DEVICE_0=mcx1.coe.neu.edu:$devid ./dwt2d rgb.bmp -d 1024x1024 -f -5 -l 3
