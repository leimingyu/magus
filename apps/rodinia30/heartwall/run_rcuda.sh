#!/bin/bash
devid=$1
RCUDA_DEVICE_0=mcx1.coe.neu.edu:$devid ./heartwall ../data/heartwall/test.avi 20
