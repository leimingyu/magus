#!/bin/bash
cp autoconf.ac_rcuda autoconf.ac
autoconf
sh ./config/conf-linux.sh 
make
