#!/bin/bash

echo "Start"

ITER=10

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
	#-----------------------
	# 1) make changes here
	#-----------------------
	./timeApp.sh ../../tests/MC_SingleAsianOptionP/MC_SingleAsianOptionP &             
	./timeApp.sh ../../tests/interval/interval &
	wait # make sure the previous background process has finished before next loop
done

### get the avg timing for each application
prefix="result_leastSim_"

#-----------------------
# 2) make changes here
#-----------------------
keyWord="MC_SingleAsianOptionP"
outFile=$prefix$keyWord
./getAvg.sh $keyWord $outFile

keyWord="interval"
outFile=$prefix$keyWord
./getAvg.sh $keyWord $outFile


echo "... ..."

#------------------------------------------------------------------------------
# most similar application
#------------------------------------------------------------------------------
#
# timeApp.sh will generate  time_log
#
if [ -f time_log ]
then
	rm time_log
fi
touch time_log


if [ -f time_log_most ]
then
	rm time_log_most
fi
touch time_log_most


for (( i=1; i<=$ITER; i++ ))
do
	#-----------------------
	# 3) make changes here
	#-----------------------
	./timeApp.sh ../../tests/MC_SingleAsianOptionP/MC_SingleAsianOptionP &             
	./timeApp.sh ../../tests/mergeSort/mergeSort &
	wait
done

prefix="result_mostSim_"

#-----------------------
# 4) make changes here
#-----------------------
keyWord="MC_SingleAsianOptionP"
outFile=$prefix$keyWord
./getAvg.sh $keyWord $outFile

keyWord="mergeSort"
outFile=$prefix$keyWord
./getAvg.sh $keyWord $outFile


echo "End"
