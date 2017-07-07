from Crypto import Random
from Crypto.Cipher import AES
import os
import random
import base64

class challenge14:
	fixed_string = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
	def __init__(self):
		self.cipher = self.gen_cipher(self.gen_key())
		self.prefix = self.gen_rand_prefix()	

	def gen_key(self):
		return Random.new().read(16)

	def gen_cipher(self,key):
		return AES.new(key)

	def gen_rand_prefix(self):
		return os.urandom(int(random.random()*100))

	def pkcs7padding(self,input,blocksize):
		num_padding = blocksize - (len(input) % blocksize)
		for c in range(num_padding):
			input += chr(c)
		return input

	def remove_padding(self,text):
		decrypted_data = text
		length_padding = ord(decrypted_data[len(decrypted_data)-1])
		return decrypted_data[0:len(decrypted_data)-length_padding]

	def encrypt_AES_128_ECB(self,plaintext, fixed_string):
			plaintext = self.prefix + plaintext + base64.b64decode(fixed_string)
			if len(plaintext) % 16 != 0:			
				plaintext = self.pkcs7padding(plaintext, AES.block_size)
				
			return self.cipher.encrypt(plaintext)


def identify_controlled_blocks(ciphertext):
	def compare_blocks(ciphertext):
		match_begin = len(ciphertext)+1
		match_end = 0
		for block1 in range(0,len(ciphertext)-16,16):
			for block2 in range(0,len(ciphertext)-16,16):
				if block1 != block2 and ciphertext[block1:block1+16] == ciphertext[block2:block2+16]:					
					if match_begin == len(ciphertext)+1:
						match_begin = block1
					else:
						match_end = block1
		return (match_begin,match_end)
	return compare_blocks(ciphertext)
				
def bruteforce_plaintext(c14,teststring,count,length):	
	for char in range(0x00,0xFF):
		ciphertext1 = c14.encrypt_AES_128_ECB(teststring+chr(char),c14.fixed_string)
		ciphertext2 = c14.encrypt_AES_128_ECB(b'A'*count,c14.fixed_string)
		
		if(ciphertext1[0:length-16] == ciphertext2[0:length-16]):
			teststring = teststring[1:length] + chr(char)
			print teststring
			return bruteforce_plaintext(c14, teststring,count-1,length)

	return teststring

def get_len(c14):
	plaintext=b'A'*64
	enc_data = c14.encrypt_AES_128_ECB(plaintext, c14.fixed_string)
	start_fixed_string = len(enc_data) - identify_controlled_blocks(enc_data)[1]
	len_fixed_string = len(enc_data) - start_fixed_string
	return len_fixed_string

c14 = challenge14()
len_fixed_string = get_len(c14)
enc_data = c14.encrypt_AES_128_ECB('A'*len_fixed_string, c14.fixed_string)
start_end_controlled = identify_controlled_blocks(enc_data)[1]
teststring = 'A' *  len_fixed_string
print bruteforce_plaintext(c14, teststring, len_fixed_string-1, len_fixed_string)
