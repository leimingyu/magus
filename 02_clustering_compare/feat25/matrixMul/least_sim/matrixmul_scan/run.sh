#!/bin/bash

echo "Start"

#ITER=10
ITER=3

#------------------------------------------------------------------------------
# least similar application
#------------------------------------------------------------------------------
#
# timeApp.sh will generate  time_log
#
if [ -f time_log ]
then
	rm time_log
fi

touch time_log



if [ -f time_log_least ]
then
	rm time_log_least
fi

touch time_log_least

for (( i=1; i<=$ITER; i++ ))
do
	echo "iter:  $i"
	#-----------------------
	# 1) make changes here
	#-----------------------
	./timeApp.sh ../../../../tests/matrixMul/matrixMul &
	./timeApp.sh ../../../../tests/scan/scan &
	wait # make sure the previous background process has finished before next loop
done

### get the avg timing for each application
prefix="result_leastSim_"

#-----------------------
# 2) make changes here
#-----------------------
keyWord="matrixMul"
outFile=$prefix$keyWord
./getAvg.sh $keyWord $outFile

keyWord="scan"
outFile=$prefix$keyWord
./getAvg.sh $keyWord $outFile

echo "End"
