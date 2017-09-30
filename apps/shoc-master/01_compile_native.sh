#!/bin/bash
cp autoconf.ac_native autoconf.ac
autoconf
sh ./config/conf-linux.sh 
make
