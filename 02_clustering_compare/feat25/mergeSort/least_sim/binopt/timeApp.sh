#!/bin/bash
runapp=$1

ts=$(date +%s%N)

### silcent the std output 
$runapp > /dev/null

runtime_ms=$((($(date +%s%N) - $ts)/1000000))

#echo -e "\n$runapp  : $runtime_ms (ms)"
echo -e "\n$runapp:$runtime_ms" >> time_log
