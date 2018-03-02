#!/bin/bash
devid=$1
RCUDA_DEVICE_0=mcx1.coe.neu.edu:$devid ./hotspot 512 2 2 ../data/hotspot/temp_512 ../data/hotspot/power_512 output.out
