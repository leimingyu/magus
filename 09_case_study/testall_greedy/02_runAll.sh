#!/bin/bash

if [ -f run2results_log ]; then
  rm run2results_log
fi

touch run2results_log

cd ./run2_tests

for file in ./*
do
	echo $file
	$file &>>  ../run2results_log 
	#break
done

echo -e  "\nDone!\nCheck run2results_log"
