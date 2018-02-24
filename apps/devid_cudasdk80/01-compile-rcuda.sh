#/bin/bash
cd 0_Simple && ./0_compile_rcuda.sh
cd ..

cd 3_Imaging && ./0_compile_rcuda.sh
cd ..

cd 4_Finance && ./0_compile_rcuda.sh
cd ..

cd 6_Advanced && ./0_compile_rcuda.sh
cd ..

cd 7_CUDALibraries && ./0_compile_rcuda.sh
cd ..
