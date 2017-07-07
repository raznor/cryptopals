import json
from Crypto.Cipher import AES
from Crypto import Random

def gen_key():
	return Random.new().read(16)

def gen_cipher(key):
	return AES.new(gen_key())

def encodeJSON(input):
	return "{\n\t" + input.replace('=',': \'').replace('&','\',\n\t') + "\n}"

def profile_for(email):
	email = email.replace("&"," ").replace("="," ")	
	return "email="+email+"&uid=10&role=user"

def pkcs7padding(input,blocksize):
	num_padding = blocksize - (len(input) % blocksize)
	for c in range(num_padding):
		input += chr(num_padding)
	return input

def enc(plaintext, cipher):
	if len(plaintext) % 16 != 0:
		plaintext = pkcs7padding(plaintext, AES.block_size)
	return cipher.encrypt(plaintext)

def dec(ciphertext, cipher):
	decrypted_data = cipher.decrypt(ciphertext)
	return decrypted_data

def remove_padding(text):
	decrypted_data = text
	length_padding = ord(decrypted_data[len(decrypted_data)-1])
	return decrypted_data[0:len(decrypted_data)-length_padding]

key = gen_key()
cipher = gen_cipher(gen_key)
encrypted_blocks = enc(profile_for("ADMINISTRAADMIN\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0bTOR"),cipher)
test = encrypted_blocks[:16] + encrypted_blocks[32:48] + encrypted_blocks[16:32]
print encodeJSON(remove_padding(dec(test,cipher)))
