#!/bin/bash

for currDir in *
do
    if [ -d $currDir ]; then
			if [ "$currDir" != "common" ];then
				cd $currDir
				make clean 
				make 
				cd ..
		fi
	fi
done
