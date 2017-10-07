#!/bin/bash

# run rcuda on mcx1
devid=$1
RCUDA_DEVICE_0=mcx1.coe.neu.edu:$devid  ./freeImageInteropNPP
