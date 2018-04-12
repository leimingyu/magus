#!/bin/bash

#=============================================================================#
# Function: obtain the avg timing
#=============================================================================#

timeApp () {
appname=$1
runapp=$2
devid=$3

ts=$(date +%s%N)
#echo -e "\n$ts" >> /tmp/magic_time_log

### silcent the std output
$runapp $devid > /dev/null

runtime_ms=$((($(date +%s%N) - $ts)/1000000))

# runtime in ms
echo -e "\n$appname:$runtime_ms" >> /tmp/magic_time_log
}


#=============================================================================#
# Function: obtain the avg timing
#=============================================================================#

getAvg()
{
local keyWord=$1
local runtime=$(awk -v pat="$keyWord"  '$0~pat{print}' /tmp/magic_time_log  | awk -F ":" '{print $2}' | awk '{ total += $1 } END { print total/NR }')
echo $runtime
}

#=============================================================================#
# create log file
#=============================================================================#
if [ -f /tmp/magic_time_log ]
then
  rm /tmp/magic_time_log
fi
touch /tmp/magic_time_log

#=============================================================================#
# benchmark the perf 
#=============================================================================#
ITER=10

app1=$1   # modify here !!!

# modify here !!!
cd $2 

for (( i=1; i<=$ITER; i++ ))
do
  timeApp $app1 ./run.sh 0 
done
app1_runtime=$(getAvg $app1)
#echo -e $app1":\t"$app1_runtime"\n"
echo -e $app1_runtime
