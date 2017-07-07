#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <inttypes.h>

void convert_str2hex(char*,uint8_t*,int);
void iter_struct(struct*);

struct {
    float a = 0.08167; 
    float b = 0.01492; 
    float c = 0.02782; 
    float d = 0.04253; 
    float e = 0.12702; 
    float f = 0.02228; 
    float g = 0.02015;  // A-G
    float h = 0.06094; 
    float i = 0.06966; 
    float j = 0.00153; 
    float k = 0.00772; 
    float l = 0.04025; 
    float m = 0.02406; 
    float n = 0.06749;  // H-N
    float o = 0.07507; 
    float p = 0.01929; 
    float q = 0.00095; 
    float r = 0.05987; 
    float s = 0.06327; 
    float t = 0.09056; 
    float u = 0.02758;  // O-U
    float v = 0.00978; 
    float w = 0.02360; 
    float x = 0.00150; 
    float y = 0.01974; 
    float z = 0.00074; 
    float whitespace = 0.01300;    
}english;

int main(int argc, char* argv[]) {
	
	char* xored = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736";
	char* tmp_xored = (char*)malloc(sizeof(char)*(strlen(xored) + strlen(xored)%2));
	
	if(strlen(xored)%2 != 0) {
		tmp_xored[0] = '0';
	}
	uint8_t *result = (char*)malloc(sizeof(char)*(strlen(xored) + strlen(xored)%2));

	strcat(tmp_xored, xored);
	convert_str2hex(tmp_xored, result, (strlen(xored) + strlen(xored)%2));
	
	return 0;
}

void iter_struct(struct* english) {

}

void get_best_scoring_key(char* xored) {
	int len = strlen(xored);
	float[len] statistic_distribution;
	int count = 0;
	for(;count<len;count++) {
		tmp = xored[count]
		int count2 = 0;
		for(;count2<len;count2++) {
			if(count2 == count) {
				continue;
			} else if (tmp == xored[count2]) {
				tmp++;
			}	
		}
	}
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