#!/usr/bin/env python


#from __future__ import print_function
import os
import sys
import argparse
import multiprocessing as mp
import subprocess
import time
from subprocess import check_call, STDOUT
import logging # logging multiprocessing 


DEVNULL = open(os.devnull, 'wb', 0) # no std out
LOGT = True # timing log

class cd:
    """
    Context manager for changing the current working directory
    """
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def run_mp(app_dir, app_cmd):
    """
    Run multiprocessing
    """
    start = time.time()
    with cd(app_dir):
        #print os.getcwd()
        check_call(app_cmd, stdout=DEVNULL, stderr=STDOUT, shell=True)
    end = time.time()
    print("{} to {} = {:.3f} seconds".format(start, end, end - start))



def run_remote(app_dir, *args):
    """
    go to app dir, and run mp for the app
    """
    arg_num = len(args)
    if arg_num > 0:
        cmd_str = ' '.join(str(e) for e in args)
        #multiprocessing.log_to_stderr(logging.DEBUG)
        p = mp.Process(target=run_mp, args=(app_dir, cmd_str))
        p.start()

    else:
        sys.exit('<Error : run_remote> No application is specified!')



#------------------------------------------------------------------------------
# tests
#------------------------------------------------------------------------------
def test1_run2():
    run_remote('../apps/rcuda_cusdk80/0_Simple/matrixMul/', './matrixMul')
    run_remote('../apps/rcuda_cusdk80/0_Simple/vectorAdd/', './vectorAdd')

def test2_selDev():
    run_remote('../apps/rcuda_cusdk80/0_Simple/matrixMul/', 
            'RCUDA_DEVICE_0=mcx1.coe.neu.edu:0', './matrixMul')
    run_remote('../apps/rcuda_cusdk80/0_Simple/vectorAdd/', 
            'RCUDA_DEVICE_0=mcx1.coe.neu.edu:1', './vectorAdd')


def tests():
    test1_run2()
    #test2_selDev()



#------------------------------------------------------------------------------
# main func 
#------------------------------------------------------------------------------
def main(arguments):
    tests()


if __name__ == "__main__":
    main(sys.argv[1:])
