#!/bin/bash
LSGINPUTS=../../inputs
devid=$1
RCUDA_DEVICE_0=mcx1.coe.neu.edu:$devid ./dmr $LSGINPUTS/250k.2 20


