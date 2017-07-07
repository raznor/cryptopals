import base64
from Crypto import Random
from Crypto.Cipher import AES
from string import ascii_lowercase
from string import printable

class challenge12:

	fixed_string = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"

	def __init__(self):
		self.key = Random.new().read(16)
		self.cipher = AES.new(self.key)

	def pkcs7padding(self,input,blocksize):
		num_padding = blocksize - (len(input) % blocksize)
		for c in range(num_padding):
			input += chr(c)
		return input

	def encrypt_AES_128_ECB(self, plaintext):
		plaintext = plaintext + base64.b64decode(self.fixed_string)
		if len(plaintext) % 16 != 0:			
			plaintext = self.pkcs7padding(plaintext, AES.block_size)
			
		return self.cipher.encrypt(plaintext)

	def oracle(self,ciphertext,size=0):
		def get3bytes(start=0):
			return bytearray(ciphertext)[start:start+size]

		matches = 0
		for count1 in range(len(ciphertext)-size):
			tup1 = get3bytes(count1)
			for count2 in range(count1+1, len(ciphertext)-size):
				tup2 = get3bytes(count2)
				if(tup1 == tup2):
					matches+=1

		if matches > 0:
			return "ECB"
		else:
			return "CBC"

def bruteforce_plaintext(c12,teststring,count,length):
	if count == 0:
		return teststring

	for char in range(0x00,0xFF):
		ciphertext1 = c12.encrypt_AES_128_ECB(teststring+chr(char))
		ciphertext2 = c12.encrypt_AES_128_ECB(b'A'*count)
		
		if(ciphertext1[0:138] == ciphertext2[0:138]):
			teststring = teststring[1:length] + chr(char)
			#print teststring
			return bruteforce_plaintext(c12, teststring,count-1,length)

	return "no match found!!!"

length = 144
count = length-1
c12 = challenge12()
teststring = b'A'*(count)
# print len(c12.encrypt_AES_128_ECB(""))
print bruteforce_plaintext(c12,teststring,count,length)
