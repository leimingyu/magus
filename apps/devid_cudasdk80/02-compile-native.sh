#/bin/bash
cd 0_Simple && ./01_compile_native.sh
cd ..

cd 3_Imaging && ./01_compile_native.sh
cd ..

cd 4_Finance && ./01_compile_native.sh
cd ..

cd 6_Advanced && ./01_compile_native.sh
cd ..

cd 7_CUDALibraries && ./01_compile_native.sh
cd ..
