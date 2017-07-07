#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <inttypes.h>

#define debug

void convert_str2hex(char*,uint8_t*,int);

int main(int argc, char* argv[]) {
	//read hex str and build buffer for it. Make an even number of chars in the buffer for later processing
	int str_size = strlen(argv[1]) + (strlen(argv[1])%2);
	uint8_t *result1 = (uint8_t*)malloc(sizeof(uint8_t)*str_size/2);
	convert_str2hex(argv[1],result1, strlen(argv[1]));

	str_size = strlen(argv[2]) + (strlen(argv[2])%2);
	uint8_t *result2 = (uint8_t*)malloc(sizeof(uint8_t)*str_size/2);
	convert_str2hex(argv[2],result2, strlen(argv[2]));	

	int count = 0;
	for(;count<str_size/2;count++) {		
		//printf("%x ^ %x = %x\n", result1[count], result2[count], result1[count] ^ result2[count]);
		printf("%x", result1[count] ^ result2[count]);
	}
	printf("\n");

	return 0;
}

void convert_str2hex(char* src, uint8_t* result, int size) {
	int str_size = size;
	char *t1;
	
	if(str_size % 2 != 0) {
		str_size += 1;
		t1 = (char*)malloc(sizeof(char)*str_size);
		t1[0] = '0';
	} else {
		t1 = (char*)malloc(sizeof(char)*str_size);	
	}

	strcat(t1,src);
	int count = 0;
	for(;count<str_size/2;count++) {
		sscanf(t1,"%2hhx", &(result[count]));
		t1+=2;
		//printf("%hhx",result[count]);
	}
	//printf("\n");
}

