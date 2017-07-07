def convert_str_to_bytes(str_val):
	tmp = bytearray()
	tmp.extend(str_val)
	return tmp

def calc_hamming_distance(bytes1, bytes2):
	hamming_distance = 0
	for index in range(len(bytes1)):
		a = bytes1[index];
		b = bytes2[index];
		for bit_count in range(0,7):
			if a & 2**bit_count != b & 2**bit_count:
				hamming_distance+=1

	return hamming_distance

def calc_best_keylength(key_range = range(1,40)):
	best_keylength = []
	for key_size in key_range:
		if calc_hamming_distance(key_size, key_size+1) == 1:
			print 1
		
def main():
	str1 = "this is a test"
	str2 = "wokka wokka!!!"
	bytes1 = convert_str_to_bytes(str1)
	bytes2 = convert_str_to_bytes(str2)
	
	hamming_distance = calc_hamming_distance(bytes1,bytes2)
	print hamming_distance

	keysize = range(2,40)



#Run This Shit
main()