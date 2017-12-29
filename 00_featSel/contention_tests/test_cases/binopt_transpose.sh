#!/bin/bash
app1="binopt"
app1_keyword="binomialOptions"
app1_cmd="../../13apps/binomialOptions/binomialOptions"

app2="transpose"
app2_keyword="transpose"
app2_cmd="../13apps/transpose/transpose"

ITER=2

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
