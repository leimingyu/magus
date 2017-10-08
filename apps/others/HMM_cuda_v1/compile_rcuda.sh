#!/bin/bash
./clean_cmake.sh
cp CMakeLists.txt_rcuda CMakeLists.txt
cmake .
make
