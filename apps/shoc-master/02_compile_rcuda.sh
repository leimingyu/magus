#!/bin/bash
make clean
cp configure.ac_rcuda configure.ac
autoconf
sh ./config/conf-linux.sh 
make
