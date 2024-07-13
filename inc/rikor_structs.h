typedef struct{
	unsigned int 		ID;
	char*				TYPE;
	char*				NAME;
	unsigned int 		COUNT;
} COMPONENT;

typedef struct{
	unsigned int 		ID;
	char*				NAME;
	COMPONENT 			PROCESSOR;
	COMPONENT 			VIDEOCARD;
	COMPONENT 			RAM;
	unsigned int 		RAM_COUNT;
	COMPONENT 			STORAGE_DEVICE;
	float 				PRICE;
} PROJECT;

typedef struct{
	unsigned int 		ID;
	PROJECT 			PROJECT;
	unsigned int 		COUNT;
} PRODUCT;

typedef struct{
	COMPONENT 			COMPONENTS[256];
	PROJECT 			PROJECTS[256];
	PRODUCT 			PRODUCTS[256];
} DATA;
