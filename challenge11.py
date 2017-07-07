from Crypto import Random
from Crypto.Cipher import AES
import base64
import random
import sys

def pkcs7padding(input, blocksize):
	num_padding = blocksize - (len(input) % blocksize)
	
	for c in range(num_padding):
		input += chr(num_padding)
	return input

def encryption(cleartext):
	header_footer= Random.new().read(random.randint(5,10))
	cleartext = header_footer + cleartext + header_footer
	if len(cleartext) % 16 != 0:
		cleartext = pkcs7padding(cleartext, AES.block_size)
	
	key = Random.new().read(16)
	iv = Random.new().read(AES.block_size)

	if(random.randint(1,2) % 2 == 0):
		print "encrypt CBC"
		cipher = AES.new(key, AES.MODE_CBC, iv)
		return iv + cipher.encrypt(cleartext)
	else:
		print "encrypt ECB"
		cipher = AES.new(key)
		return cipher.encrypt(cleartext)

def oracle(ciphertext, size):
	#print dbg_print(ciphertext)
	def get3bytes(start=0):
		return bytearray(ciphertext)[start:start+size]

	matches = 0
	for count1 in range(len(ciphertext)-size):
		tup1 = get3bytes(count1)
		for count2 in range(count1+1, len(ciphertext)-size):
			tup2 = get3bytes(count2)
			#print (count1,count2,tup1,tup2)
			if(tup1 == tup2):
				#print "count1: {} count2: {}".format(count1,count2)
				#print "tup1: {} tup2: {}".format(dbg_print(tup1),dbg_print(tup2))
				matches+=1

	if matches > 0:
		print "Oracle: ECB"
	else:
		print "Oracle: CBC"
	return 

oracle(encryption(b'YELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINE'),3)

