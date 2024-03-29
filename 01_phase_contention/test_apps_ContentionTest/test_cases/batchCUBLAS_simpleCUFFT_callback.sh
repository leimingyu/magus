#!/bin/bash
app1="batchCUBLAS"
app1_keyword="batchCUBLAS"
app1_cmd="../../test_apps/batchCUBLAS/batchCUBLAS"

app2="simpleCUFFT_callback"
app2_keyword="simpleCUFFT_callback"
app2_cmd="../../test_apps/simpleCUFFT_callback/simpleCUFFT_callback"

ITER=50

if [ -f time_log ]
then
  rm time_log
fi
touch time_log

for (( i=1; i<=$ITER; i++ ))
do
  ../timeApp.sh ${app1_cmd} &
  ../timeApp.sh ${app2_cmd} &
  wait
done

getAvg()
{
local keyWord=$1
local runtime=$(awk -v pat="$keyWord"  '$0~pat{print}' time_log  | awk -F ":" '{print $2}' | awk '{ total += $1 } END { print total/NR }')
echo $runtime
}

testName=$app1"_"$app2

app1_runtime=$(getAvg $app1_keyword)
app2_runtime=$(getAvg $app2_keyword)

echo -e $testName": \t"$app1": "$app1_runtime"\t"$app2": "$app2_runtime
