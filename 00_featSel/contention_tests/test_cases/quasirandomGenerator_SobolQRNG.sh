#!/bin/bash
app1="quasirandomGenerator"
app1_keyword="quasirandomGenerator"
app1_cmd="../../13apps/quasirandomGenerator/quasirandomGenerator"

app2="SobolQRNG"
app2_keyword="SobolQRNG"
app2_cmd="../../13apps/SobolQRNG/SobolQRNG"

ITER=20

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
