#!/bin/bash

# input
inputFile=$1

echo "cpu (ms)"
# read line contain cpu, get timing from the last field, extract floats
grep "\[cpu" $inputFile | awk -F " "  '{print $NF}' | grep -Eo '[+-]?[0-9]+([.][0-9]+)?' | awk '{ total += $1; } END { print total }'



echo "gpu (ms)"
# read line contain cpu, get timing from the last field, extract floats
grep "\[gpu" $inputFile | awk -F " "  '{print $NF}' | grep -Eo '[+-]?[0-9]+([.][0-9]+)?' | awk '{ total += $1; } END { print total }'

