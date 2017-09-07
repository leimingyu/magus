#!/bin/bash
#app1=$1
#app2=$2


# test 1 :
# ./SobolQRNG/SobolQRNG
# ./MC_SingleAsianOptionP/MC_SingleAsianOptionP 


./timeApp.sh ./SobolQRNG/SobolQRNG &
./timeApp.sh ./MC_SingleAsianOptionP/MC_SingleAsianOptionP &



#if [ -f /tmp/magus_timing_log ]
#then
#	rm /tmp/magus_timing_log 
#	touch /tmp/magus_timing_log 
#fi
#
#ITER=10
#
#for (( n=1; n<=$ITER; n++ ))
#do
#	ts=$(date +%s%N) 
#
#	$runapp
#
#	runtime_ms=$((($(date +%s%N) - $ts)/1000000)) 
#
#	echo "$runtime_ms"  >> /tmp/magus_timing_log 
#done
#
#awk '{ total += $1; count++ } END { print total/count }' /tmp/magus_timing_log | tee qtest_timing_ms 
