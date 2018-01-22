#!/bin/bash
app1="convolutionSeparable"
app1_keyword="convolutionSeparable"
app1_cmd="../../test_apps/convolutionSeparable/convolutionSeparable"

ITER=100

if [ -f time_log ]
then
  rm time_log
fi
touch time_log

for (( i=1; i<=$ITER; i++ ))
do
  ../timeApp.sh ${app1_cmd} &
  wait
done

getAvg()
{
local keyWord=$1
local runtime=$(awk -v pat="$keyWord"  '$0~pat{print}' time_log  | awk -F ":" '{print $2}' | awk '{ total += $1 } END { print total/NR }')
echo $runtime
}

testName=$app1

app1_runtime=$(getAvg $app1_keyword)

echo -e $testName": \t"$app1": "$app1_runtime