#!/usr/bin/env python


#from __future__ import print_function
import os
import sys
import argparse
import multiprocessing
import subprocess
import time
from subprocess import check_call, STDOUT
import logging # logging multiprocessing 



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

    print "arg number :  " + str(len(args))

    with cd(app_dir):
        #print os.getcwd()
        if len(args) == 0:
            check_call([app_cmd], stdout=DEVNULL, stderr=STDOUT)
        else:
            app_cmd_list = [app_cmd]
            for arg in args:
                app_cmd_list.append(arg)

            print app_cmd_list

            check_call(app_cmd_list, stdout=DEVNULL, stderr=STDOUT)
            #check_call(app_cmd_list, stdout=DEVNULL, stderr=STDOUT, shell=True)

    end = time.time()
    print("{} to {} = {:.3f} seconds".format(start, end, end - start))


def test1_run2():
    std_out = open(os.devnull, 'wb', 0)
    p = multiprocessing.Process(target=run_remote_mp, args=(std_out,
        '../apps/rcuda_cusdk80/0_Simple/matrixMul/',
        './matrixMul'))
    p.start()

    p = multiprocessing.Process(target=run_remote_mp, args=(std_out,
        '../apps/rcuda_cusdk80/0_Simple/vectorAdd/',
        './vectorAdd'))
    p.start()

def test2_selDev():
    #multiprocessing.log_to_stderr(logging.DEBUG)
    std_out = open(os.devnull, 'wb', 0)
    p = multiprocessing.Process(target=run_remote_mp, args=(std_out,
        '../apps/rcuda_cusdk80/0_Simple/matrixMul/',
        'RCUDA_DEVICE_0=mcx1.coe.neu.edu:0',
        './matrixMul'))
    p.start()


def tests():
    #test1_run2()
    test2_selDev()


def main(arguments):
    tests()


if __name__ == "__main__":
    main(sys.argv[1:])
