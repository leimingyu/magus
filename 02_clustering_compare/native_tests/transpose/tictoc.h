#ifndef __TICTOC_H_
#define __TICTOC_H_

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>

#ifdef  __cplusplus
extern "C" {
#endif
                                                                                
double getCpuTime();

double getCpuTime()
{
	struct timeval tv;
	gettimeofday(&tv,NULL);
	// return milliseconds
	return (double)(tv.tv_sec) * 1000 + (double)(tv.tv_usec) / 1000;
}

                                                                                
#ifdef  __cplusplus
}
#endif

#endif
