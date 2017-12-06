#!/bin/bash
LSGINPUTS=../../inputs
devid=$1
RCUDA_DEVICE_0=mcx1.coe.neu.edu:$devid ./mst $LSGINPUTS/rmat12.sym.gr 


