#!/bin/bash
devid=$1
RCUDA_DEVICE_0=mcx1.coe.neu.edu:$devid ./b+tree.out file ../data/b+tree/mil.txt command ../data/b+tree/command.txt
