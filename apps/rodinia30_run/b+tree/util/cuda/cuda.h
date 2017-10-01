#ifdef __cplusplus
extern "C" {
#endif

//===============================================================================================================================================================================================================200
//	SET_DEVICE HEADER
//===============================================================================================================================================================================================================200

//======================================================================================================================================================150
//	INCLUDE/DEFINE
//======================================================================================================================================================150

#include <stdio.h>					// (in library path known to compiler)		needed by printf

//======================================================================================================================================================150
//	FUNCTION PROTOTYPES
//======================================================================================================================================================150

//====================================================================================================100
//	SET DEVICE
//====================================================================================================100

void setdevice(void);

//====================================================================================================100
//	GET LAST ERROR
//====================================================================================================100

void checkCUDAError(const char *msg);

//===============================================================================================================================================================================================================200
//	END SET_DEVICE HEADER
//===============================================================================================================================================================================================================200

#ifdef __cplusplus
}
#endif
