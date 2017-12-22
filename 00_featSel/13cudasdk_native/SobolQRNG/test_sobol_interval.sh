#!/bin/bash

MAXITER=10

echo "check file in /tmp/appname"$BASHPID


filename=$BASHPID


### 1) run multiple tests
for (( i=0; i<MAXITER; i++ ))
do
./SobolQRNG  >> /tmp/sobol$filename 2>&1 &
../interval/interval >> /tmp/interval$filename 2>&1 &
wait  
done


### 2) sum up all the cpu and gpu time and get avg
#../getCpuGpuTiming.sh /tmp/$filename $MAXITER
echo "sobol results"
./getCpuGpuTiming.sh /tmp/sobol$filename $MAXITER

echo "interval results"
./getCpuGpuTiming.sh /tmp/interval$filename $MAXITER


