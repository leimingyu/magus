#!/bin/bash


for currDir in *
do
    if [ -d $currDir ]; then
			if [ "$currDir" != "common" ] &&  [ "$currDir" != "data" ] &&  [ "$currDir" != "metrics" ] &&  [ "$currDir" != "traces" ] ;then
				echo -e "\n\n=> go to $currDir"
				cd $currDir
				./profile-this.sh
				cd ..
		fi
	fi
done



