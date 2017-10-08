#!/bin/bash
./clean_cmake.sh
cp CMakeLists.txt_native CMakeLists.txt
cmake .
make
