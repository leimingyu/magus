#!/bin/bash
runapp=$1

if [ -f /tmp/magus_timing_log ]
then
	rm /tmp/magus_timing_log 
	touch /tmp/magus_timing_log 
fi

ITER=10
#ITER=5

for (( n=1; n<=$ITER; n++ ))
do
	ts=$(date +%s%N) 

	$runapp

	runtime_ms=$((($(date +%s%N) - $ts)/1000000)) 

	echo "$runtime_ms"  >> /tmp/magus_timing_log 
done

echo ""
echo ""
echo ""
awk '{ total += $1; count++ } END { print total/count }' /tmp/magus_timing_log | tee qtest_timing_ms 
