#!/bin/bash

# input
inputFile=$1

iters=$2
echo "iters : "$iters

echo "cpu (ms)"
# read line contain cpu, get timing from the last field, extract floats
grep "\[cpu" $inputFile | awk -F " "  '{print $NF}' | grep -Eo '[+-]?[0-9]+([.][0-9]+)?' | awk '{ total += $1; } END { print total/"'${iters}'" }'



echo "gpu (ms)"
# read line contain cpu, get timing from the last field, extract floats
grep "\[gpu" $inputFile | awk -F " "  '{print $NF}' | grep -Eo '[+-]?[0-9]+([.][0-9]+)?' | awk '{ total += $1; } END { print total/"'${iters}'" }'

