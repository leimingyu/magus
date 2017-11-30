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
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


def run_remote_mp(DEVNULL, app_dir, app_cmd, *args):
    start = time.time()
    with cd(app_dir):
        #print os.getcwd()
        if len(args) == 0:
            # directly run the command 
            check_call([app_cmd], stdout=DEVNULL, stderr=STDOUT)
        else:
            app_cmd_list = [app_cmd]
            for arg in args:
                app_cmd_list.append(arg)
            #concatenate the cmds into one string (including env var) 
            cmd_str = ' '.join(str(e) for e in app_cmd_list)
            check_call(cmd_str, stdout=DEVNULL, stderr=STDOUT, shell=True)

    end = time.time()
    print("{} to {} = {:.3f} seconds".format(start, end, end - start))


def run_mp(app_dir, app_cmd):
    """
    run multiprocessing
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
        p = mp.Process(target=run_mp, args=(app_dir, cmd_str))
        p.start()

    else:
        sys.exit('<Error : run_remote> No application is specified!')



#------------------------------------------------------------------------------
# tests
#------------------------------------------------------------------------------
def test1_run2():
    p = mp.Process(target=run_remote_mp, args=(std_out,
        '../apps/rcuda_cusdk80/0_Simple/matrixMul/',
        './matrixMul'))
    p.start()

    p = mp.Process(target=run_remote_mp, args=(std_out,
        '../apps/rcuda_cusdk80/0_Simple/vectorAdd/',
        './vectorAdd'))
    p.start()

def test2_selDev():
    #multiprocessing.log_to_stderr(logging.DEBUG)
    p = mp.Process(target=run_remote_mp, args=(std_out,
        '../apps/rcuda_cusdk80/0_Simple/matrixMul/',
        'RCUDA_DEVICE_0=mcx1.coe.neu.edu:0',
        './matrixMul'))
    p.start()
    p = mp.Process(target=run_remote_mp, args=(std_out,
        '../apps/rcuda_cusdk80/0_Simple/vectorAdd/',
        'RCUDA_DEVICE_0=mcx1.coe.neu.edu:1',
        './vectorAdd'))
    p.start()

def test3():
    #run_remote('../apps/rcuda_cusdk80/0_Simple/vectorAdd/', './vectorAdd')

    #run_remote('../apps/rcuda_cusdk80/0_Simple/vectorAdd/', 
    #        'RCUDA_DEVICE_0=mcx1.coe.neu.edu:0',
    #        './vectorAdd')


def tests():
    #test1_run2()
    #test2_selDev()
    test3()



#------------------------------------------------------------------------------
# main func 
#------------------------------------------------------------------------------
def main(arguments):
    tests()


if __name__ == "__main__":
    main(sys.argv[1:])
