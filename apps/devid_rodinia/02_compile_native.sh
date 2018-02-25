#!/bin/bash


for currDir in *
do
    if [ -d $currDir ]; then
			if [ "$currDir" != "common" ] &&  [ "$currDir" != "data" ] ;then
				echo -e "\n\n=> go to $currDir"
				cd $currDir
				make clean 
				make
				cd ..
		fi
	fi
done



