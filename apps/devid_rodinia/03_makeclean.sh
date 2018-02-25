#!/bin/bash


for currDir in *
do
    if [ -d $currDir ]; then
			if [ "$currDir" != "common" ] &&  [ "$currDir" != "data" ] ;then
				cd $currDir
				make clean
				cd ..
		fi
	fi
done



