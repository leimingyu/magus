#!/bin/bash

#
# cudasdk 80
#
echo -e "\n#---------------#"
echo -e "# cudasdk 80"
echo -e "#---------------#\n"
cd ../apps/devid_cudasdk80  
./03-makeclean.sh 
#./02-compile-native.sh
cd ../

#
# lonestar
#
echo -e "\n#---------------#"
echo -e "# lonestar "
echo -e "#---------------#\n"
cd devid_lonestar/ 
./03_makeclean.sh
#./02_compile_native.sh
cd ..

#
# rodinia 
#
echo -e "\n#---------------#"
echo -e "# rodinia"
echo -e "#---------------#\n"
cd devid_rodinia/ 
./03_makeclean.sh
#./02_compile_native.sh
cd ..


#
# shoc 
#
echo -e "\n#---------------#"
echo -e "# shoc"
echo -e "#---------------#\n"
cd devid_shoc/
make clean
#./01_compile_native.sh
cd ..


#
# parboil 
#
echo -e "\n#---------------#"
echo -e "# parboil"
echo -e "#---------------#\n"
cd devid_parboil/
./03_makeclean.sh
#./02-compile-native.sh
cd ..


#
# poly 
#
echo -e "\n#---------------#"
echo -e "# poly"
echo -e "#---------------#\n"
cd devid_poly/
./03_makeclean.sh
#./02-compile-native.sh
cd ..
