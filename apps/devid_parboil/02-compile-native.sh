#!/bin/bash

cd benchmarks

for currDir in *
do
    if [ -d $currDir ];then
		#echo $currDir 
		if [ "$currDir" != "others_" ]; then
			cd $currDir
			make clean
			make
			cd ..
		fi
    fi
done
