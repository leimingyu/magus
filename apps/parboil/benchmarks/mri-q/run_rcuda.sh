#!/bin/bash
devid=$1
RCUDA_DEVICE_0=mcx1.coe.neu.edu:$devid ./mri-q -i ../../datasets/mri-q/small/input/32_32_32_dataset.bin
