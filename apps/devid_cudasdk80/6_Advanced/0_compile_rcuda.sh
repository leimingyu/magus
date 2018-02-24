#!/bin/bash

for currDir in *
do
    if [ -d $currDir ]; then
			if [ "$currDir" != "common" ] &&\
				[ "$currDir" != "lineOfSight" ];then
				cd $currDir
				make clean && make EXTRA_NVCCFLAGS=--cudart=shared
				cd ..
		fi
	fi
done
