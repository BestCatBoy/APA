# ifndef sort_data_h_
# define sort_data_h_

# include <stdlib.h>
# include <stdio.h>
# include <string.h>

# include "rikor_structs.h"

COMPONENT GET_COMPONENT(
		unsigned int 	ID,
		char*			TYPE,
		char*			NAME,
		unsigned int 	COUNT);

PROJECT GET_PROJECT(
		unsigned int 	ID,
		char*			NAME,
		COMPONENT 		PROCESSOR,
		COMPONENT 		VIDEOCARD,
		COMPONENT 		RAM,
		unsigned int 	RAM_COUNT,
		COMPONENT 		STORAGE_DEVICE,
		float 			PRICE);

PRODUCT GET_PRODUCT(
		unsigned int 	ID,
		PROJECT 		PROJECT,
		unsigned int 	COUNT);

DATA GET_DATA(
		COMPONENT* 		COMPONENTS,
		PROJECT* 		PROJECTS,
		PRODUCT* 		PRODUCTS);

# endif
