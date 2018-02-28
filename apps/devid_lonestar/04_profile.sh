#!/bin/bash

##download inputs
#make inputs

cd apps/

for currDir in *
do
    if [ -d $currDir ]; then
			if [ "$currDir" != "scripts" ];then
				cd $currDir
				# profile app
				./profile-this.sh
				cd ..
		fi
	fi
done

