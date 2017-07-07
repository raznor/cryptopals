#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>

void print_binary(uint8_t);
void map_to_b64enc(uint8_t*,uint8_t*, int);
void build_index(uint8_t*,uint8_t*, int);
int get_size_of_b64enc_str(uint8_t*);
int get_size_of_str(char*);

int get_size_of_str(char* str) {
	int size = 0;
	while(str[size++] != 0);
	return size-1; //remove null byte count
}

int get_size_of_b64enc_str(uint8_t* str) {
	int size = 0;
	int sizeb64 = 0;
	while(str[size++] != 0);
	size--; //remove null byte count
//	printf("size is %d\n",size);
	while (size-3 > 0) {
		size-=3;
		sizeb64 +=4;
	}	

	if(size != 0) {
		sizeb64 += 4;
	}	

	return sizeb64;
}

void build_index(uint8_t* org, uint8_t* base64, int tmp_index) {

	//no padding
	uint8_t p1 = org[0] >> 2;

	uint8_t tmp1 = org[0] << 6;
	uint8_t tmp2 = org[1] >> 4;
	uint8_t p2 = (tmp1 >> 2) | (tmp2);
	
	tmp1 = org[1] << 4;
	tmp2 = org[2] >> 6;
	uint8_t p3 = (tmp1 >> 2) | (tmp2);

	uint8_t tmp4 = org[2] << 2;
	uint8_t p4 = tmp4 >> 2;

//	printf("tmp_index: %d\n",tmp_index);

	base64[tmp_index]= p1;
	base64[tmp_index + 1]= p2;
	base64[tmp_index + 2]= p3;
	base64[tmp_index + 3]= p4;

/*	
	print_binary(p1); 
	print_binary(p2); 
	print_binary(p3); 
	print_binary(p4); 

	printf("%u\n",p1);
	printf("%u\n",p2);
	printf("%u\n",p3);
	printf("%u\n",p4);
*/
}

void map_to_b64enc(uint8_t* index, uint8_t* b64enc, int sizeb64) {
	int count = 0;
	for(;count < sizeb64; count++) {
		if(index[count] < 26) { //A-Z
			b64enc[count] = index[count] + 65;

		} else if (index[count] < 52){ //a-z
			b64enc[count] = index[count] + 71;

		} else if (index[count] < 62) { //0-9
			b64enc[count] = index[count] - 4;

		} else if(index[count] == 63) { // +
			b64enc[count] = 43;

		} else if(index[count] == 64) { // /
			b64enc[count] = 47;

		} else {
			printf("!!! ERROR !!!");
		}
		printf("count= %d value is: %c\n", count, b64enc[count]);
	}

	printf("sizeb64%d\n", sizeb64);
	if(index[sizeb64-1] == 0 ) {
		b64enc[sizeb64-1] = 61;
	}
	
	if(index[sizeb64-2] == 0 && index[sizeb64 -1] == 0) {
		b64enc[sizeb64-2] = 61;
	}

}

void print_binary(uint8_t byte) {
	int count = 7;
	while(count >= 0) {
		uint8_t tmp = byte << (7-count);
		uint8_t result = tmp >> 7;
		printf("%d",result);
		count--;
	}
	printf("\n");
}

int encode(char* str_to_enc, uint8_t* encoded) {
	
	int size_of_str = get_size_of_str(str_to_enc);
	int sizeb64 = get_size_of_b64enc_str((uint8_t*)str_to_enc);

	printf("size of encoded is: %d\n", sizeb64);
	
	int count = 0;
	int count_encoded = 0;
	int count_index = 0;
	uint8_t tmp_index[sizeb64];
	//
	printf("tmp_index is : %i\n", sizeb64);	
	//
	for(; count < size_of_str; count+=3) {
		uint8_t tmp[3];
		//potential seg fault
		tmp[0] = str_to_enc[count];
		tmp[1] = 0;
		tmp[2] = 0;
		if (count + 1 < size_of_str) {
			tmp[1] = str_to_enc[count+1];
		} 
		if (count + 2 < size_of_str) {
			tmp[2] = str_to_enc[count+2];
		} 

		printf("tmp[0]: %c tmp[1]: %c tmp[2]: %c\n", tmp[0], tmp[1], tmp[2]);

		build_index((uint8_t*)&tmp, (uint8_t*)&tmp_index, count_index);
		count_index += 4;
	}
	
	map_to_b64enc((uint8_t*)&tmp_index, encoded, sizeb64);
	
	return sizeb64;
} 

int main(int argc, char* argv[]) {
	char* str_to_enc= argv[1];
#if 0
	uint8_t* hexstring;// (uint8_t*)malloc(sizeof(uint8_t)*get_size_of_str(str_to_enc));
	unsigned long int result =(unsigned long int) strtol(str_to_enc, NULL, 16);
	hexstring = (uint8_t*) &result;	
#endif
	int sizeb64 = get_size_of_b64enc_str(str_to_enc);
	printf("allocating %zd\n", sizeof(uint8_t)*sizeb64);
        uint8_t* encoded = (uint8_t*)malloc(sizeof(uint8_t) * sizeb64);

	int size_encoded_str = encode(str_to_enc, encoded);
//	printf("size of encoded str is : %d", size_encoded_str);
	int count = 0;
	for(;count < size_encoded_str;count++) {
		printf("%c",(char)encoded[count]);
	}
	printf("\n");
	free(encoded);
}	
