#!/bin/bash

cd benchmarks/

for currDir in *
do
    if [ -d $currDir ];then
		#echo $currDir 
		if [ "$currDir" != "others_" ]; then
			cd $currDir
			./profile-this.sh
			cd ..
		fi
    fi
done

echo -e "\n\n"
echo "All done"
