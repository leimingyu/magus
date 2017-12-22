#!/bin/bash

MAXITER=10

echo "check file in /tmp/magus_"$BASHPID


filename=$BASHPID


### 1) run multiple tests
for (( i=0; i<MAXITER; i++ ))
do
  ./interval >> /tmp/magus$filename
  sleep 1s
done


### 2) sum up all the cpu and gpu time and get avg
#../getCpuGpuTiming.sh /tmp/$filename $MAXITER
./getCpuGpuTiming.sh /tmp/magus$filename $MAXITER



