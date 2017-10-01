#!/bin/bash

for currDir in *
do
    echo $currDir
    if [ -d $currDir ]
	then
		cd $currDir
		pwd
		make clean
		make
		./1_nvprof_current.sh	
		mv *.csv ../
		cd ..
    fi
	echo "profiling done"
done
echo "All done"
