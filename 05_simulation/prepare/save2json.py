#!/usr/bin/env python
"""Edit gpu workloads and save to a json file"""

import sys
sys.path.append('../protobuf')
import GPUApp_pb2

from google.protobuf.json_format import MessageToJson
from google.protobuf.internal.encoder import _VarintBytes

outputFile = 'app_info.bin'

appList = []

appList.append(GPUApp_pb2.GPUApp(
    dir='../apps/rcuda_cusdk80/0_Simple/matrixMul',
    cmd='matrixMul'))

appList.append(GPUApp_pb2.GPUApp(
    dir='../apps/rcuda_cusdk80/0_Simple/vectorAdd',
    cmd='vectorAdd'))

appList.append(GPUApp_pb2.GPUApp(
    dir='../apps/rcuda_cusdk80/0_Simple/test',
    cmd='leiming'))


with open(outputFile, 'wb') as f:
    for curApp in appList:
        size = curApp.ByteSize()
        f.write(_VarintBytes(size))
        f.write(curApp.SerializeToString())


#from google.protobuf.internal.decoder import _DecodeVarint32
#
#read_app_list = []
#with open(outputFile, 'rb') as f:
#    buf = f.read()
#    n = 0
#    while n < len(buf): 
#        msg_len, new_pos = _DecodeVarint32(buf, n)
#        n = new_pos
#        msg_buf = buf[n:n+msg_len]
#        n += msg_len
#        curApp = GPUApp_pb2.GPUApp()
#        curApp.ParseFromString(msg_buf)
#        read_app_list.append(curApp)
#
#print "\n\nreading"
#print read_app_list
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