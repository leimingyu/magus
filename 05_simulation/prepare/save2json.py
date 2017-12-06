#!/usr/bin/env python
"""Edit gpu workloads and save to a json file"""

import sys
from google.protobuf.internal.encoder import _VarintBytes
sys.path.append('../protobuf')
import GPUApp_pb2

outputFile = 'app_info.bin'

appList = []

appList.append(GPUApp_pb2.GPUApp(
    name='matrixMul',
    dir='../apps/rcuda_cusdk80/0_Simple/matrixMul',
    cmd='matrixMul'))

appList.append(GPUApp_pb2.GPUApp(
    name='vectorAdd',
    dir='../apps/rcuda_cusdk80/0_Simple/vectorAdd',
    cmd='vectorAdd'))


with open(outputFile, 'wb') as f:
    for curApp in appList:
        size = curApp.ByteSize()
        f.write(_VarintBytes(size))
        f.write(curApp.SerializeToString())



#
#
#print "1st"
##print read_app_list[0]
#curApp = read_app_list[0]
#print curApp.dir
#print curApp.cmd
#
#print "2nd"
#print read_app_list[1]