/*
 * Copyright 1993-2015 NVIDIA Corporation.  All rights reserved.
 *
 * Please refer to the NVIDIA end user license agreement (EULA) associated
 * with this source code for terms and conditions that govern your use of
 * this software. Any use, reproduction, disclosure, or distribution of
 * this software and related documentation outside the terms of the EULA
 * is strictly prohibited.
 *
 */



#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <cuda_runtime.h>
#include <helper_functions.h>
#include <helper_cuda.h>
#include "mergeSort_common.h"

#include "../tictoc.h"
#define LOG 1

////////////////////////////////////////////////////////////////////////////////
// Test driver
////////////////////////////////////////////////////////////////////////////////
int main(int argc, char **argv)
{
    uint *h_SrcKey, *h_SrcVal, *h_DstKey, *h_DstVal;
    uint *d_SrcKey, *d_SrcVal, *d_BufKey, *d_BufVal, *d_DstKey, *d_DstVal;
    StopWatchInterface *hTimer = NULL;

    const uint   N = 4 * 1048576;
    const uint DIR = 1;
    const uint numValues = 65536;

    printf("%s Starting...\n\n", argv[0]);

    int dev = findCudaDevice(argc, (const char **) argv);

    if (dev == -1)
    {
        return EXIT_FAILURE;
    }

#if LOG
    double tic,toc;
    tic = getCpuTime();
#endif

    printf("Allocating and initializing host arrays...\n\n");
    sdkCreateTimer(&hTimer);
    h_SrcKey = (uint *)malloc(N * sizeof(uint));
    h_SrcVal = (uint *)malloc(N * sizeof(uint));
    h_DstKey = (uint *)malloc(N * sizeof(uint));
    h_DstVal = (uint *)malloc(N * sizeof(uint));

    srand(2009);

    for (uint i = 0; i < N; i++)
    {
        h_SrcKey[i] = rand() % numValues;
    }

    fillValues(h_SrcVal, N);

#if LOG
    toc = getCpuTime();
    fprintf(stdout, "\n[cpu malloc and init (ms) : %lf]\n", toc - tic);
#endif

#if LOG
    tic = getCpuTime();
#endif
    printf("Allocating and initializing CUDA arrays...\n\n");
    checkCudaErrors(cudaMalloc((void **)&d_DstKey, N * sizeof(uint)));
    checkCudaErrors(cudaMalloc((void **)&d_DstVal, N * sizeof(uint)));
    checkCudaErrors(cudaMalloc((void **)&d_BufKey, N * sizeof(uint)));
    checkCudaErrors(cudaMalloc((void **)&d_BufVal, N * sizeof(uint)));
    checkCudaErrors(cudaMalloc((void **)&d_SrcKey, N * sizeof(uint)));
    checkCudaErrors(cudaMalloc((void **)&d_SrcVal, N * sizeof(uint)));
#if LOG
    toc = getCpuTime();
    fprintf(stdout, "\n[gpu malloc (ms) : %lf]\n", toc - tic);
#endif



#if LOG
    tic = getCpuTime();
#endif
    checkCudaErrors(cudaMemcpy(d_SrcKey, h_SrcKey, N * sizeof(uint), cudaMemcpyHostToDevice));
    checkCudaErrors(cudaMemcpy(d_SrcVal, h_SrcVal, N * sizeof(uint), cudaMemcpyHostToDevice));

#if LOG
    toc = getCpuTime();
    fprintf(stdout, "\n[gpu h2d (ms) : %lf]\n", toc - tic);
#endif

    printf("Initializing GPU merge sort...\n");

#if LOG
    tic = getCpuTime();
#endif
    initMergeSort();
#if LOG
    toc = getCpuTime();
    fprintf(stdout, "\n[gpu malloc (ms) : %lf]\n", toc - tic);
#endif

    printf("Running GPU merge sort...\n");
    checkCudaErrors(cudaDeviceSynchronize());
    sdkResetTimer(&hTimer);
    sdkStartTimer(&hTimer);

#if LOG
    tic = getCpuTime();
#endif

    mergeSort(
        d_DstKey,
        d_DstVal,
        d_BufKey,
        d_BufVal,
        d_SrcKey,
        d_SrcVal,
        N,
        DIR
    );
#if LOG
    toc = getCpuTime();
    fprintf(stdout, "\n[gpu compute and d2d (ms) : %lf]\n", toc - tic);
#endif


    checkCudaErrors(cudaDeviceSynchronize());
    sdkStopTimer(&hTimer);
    printf("Time: %f ms\n", sdkGetTimerValue(&hTimer));

    printf("Reading back GPU merge sort results...\n");

#if LOG
    tic = getCpuTime();
#endif
    checkCudaErrors(cudaMemcpy(h_DstKey, d_DstKey, N * sizeof(uint), cudaMemcpyDeviceToHost));
    checkCudaErrors(cudaMemcpy(h_DstVal, d_DstVal, N * sizeof(uint), cudaMemcpyDeviceToHost));

#if LOG
    toc = getCpuTime();
    fprintf(stdout, "\n[gpu compute and d2d (ms) : %lf]\n", toc - tic);
#endif

    printf("Inspecting the results...\n");

#if LOG
    tic = getCpuTime();
#endif
    uint keysFlag = validateSortedKeys(
                        h_DstKey,
                        h_SrcKey,
                        1,
                        N,
                        numValues,
                        DIR
                    );

    uint valuesFlag = validateSortedValues(
                          h_DstKey,
                          h_DstVal,
                          h_SrcKey,
                          1,
                          N
                      );

#if LOG
    toc = getCpuTime();
    fprintf(stdout, "\n[cpu validation (ms) : %lf]\n", toc - tic);
#endif

    printf("Shutting down...\n");


#if LOG
    tic = getCpuTime();
#endif
    closeMergeSort();
    sdkDeleteTimer(&hTimer);
    checkCudaErrors(cudaFree(d_SrcVal));
    checkCudaErrors(cudaFree(d_SrcKey));
    checkCudaErrors(cudaFree(d_BufVal));
    checkCudaErrors(cudaFree(d_BufKey));
    checkCudaErrors(cudaFree(d_DstVal));
    checkCudaErrors(cudaFree(d_DstKey));

#if LOG
    toc = getCpuTime();
    fprintf(stdout, "\n[gpu free (ms) : %lf]\n", toc - tic);
#endif


#if LOG
    tic = getCpuTime();
#endif
    free(h_DstVal);
    free(h_DstKey);
    free(h_SrcVal);
    free(h_SrcKey);

#if LOG
    toc = getCpuTime();
    fprintf(stdout, "\n[cpu free (ms) : %lf]\n", toc - tic);
#endif

    exit((keysFlag && valuesFlag) ? EXIT_SUCCESS : EXIT_FAILURE);
}
