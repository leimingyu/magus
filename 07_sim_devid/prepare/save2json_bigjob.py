#!/usr/bin/env python
"""Edit gpu workloads and save to a json file"""

import sys
from google.protobuf.internal.encoder import _VarintBytes
sys.path.append('../protobuf')
import GPUApp_pb2

outputFile = 'bigjob_info.bin'

appList = []

#------------------------------------------------------------------------------
# cuda sdk 8.0:  ``$./run.sh devid``
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_convolutionFFT2D', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_convolutionSeparable', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_stereoDisparity', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_binomialOptions', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_fastWalshTransform', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_FDTD3d', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_interval', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_radixSortThrust', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_scan', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_segmentationTreeThrust', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_sortingNetworks', dir='',cmd=''))

#------------------------------------------------------------------------------
# polybench 
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(name='poly_3mm', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='poly_correlation', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='poly_covariance', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='poly_fdtd2d', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='poly_syr2k', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='poly_syrk', dir='',cmd=''))


#------------------------------------------------------------------------------
# lonestar 
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(name='lonestar_dmr', dir='',cmd=''))

#------------------------------------------------------------------------------
# parboil 
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(name='parboil_lbm', dir='',cmd=''))


#------------------------------------------------------------------------------
# others 
#------------------------------------------------------------------------------



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
