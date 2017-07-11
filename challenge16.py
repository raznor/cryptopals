import binascii
from Crypto.Cipher import AES
from Crypto import Random

class challenge16:
	PREFIX="comment1=cooking%20MCs;userdata="
	POSTFIX=";comment2=%20like%20a%20pound%20of%20bacon"
	IS_ADMIN =";admin=true;"

	def __init__(self):
		self.SECRET_KEY = Random.new().read(16)
		self.IV = Random.new().read(16)
		self.cipher_for_encryption = AES.new(self.SECRET_KEY, AES.MODE_CBC, self.IV)
		self.cipher_for_decryption = AES.new(self.SECRET_KEY, AES.MODE_CBC, self.IV)

	def encrypt(self, plaintxt):
		def pkcs7padding(input,blocksize):
			num_padding = blocksize - (len(input) % blocksize)
			for c in range(num_padding):
				input += chr(c)
			return input

		return self.cipher_for_encryption.encrypt(pkcs7padding(plaintxt, 16))

	def decrypt(self, ciphertxt):
		return self.cipher_for_decryption.decrypt(ciphertxt)

	def enc_userinput(self, userinput):
		def sanitize_userinput(userinput):
			return userinput.replace("=","\"=\"").replace(";","\";\"")
		
		self.full_str = self.PREFIX+sanitize_userinput(userinput)+self.POSTFIX
		return self.encrypt(self.full_str)

	def is_admin(self,plaintxt):
		if self.IS_ADMIN in plaintxt:
			return True
		return False

class helper_cls:
	def sxor(self,s1,s2):    
	    # convert strings to a list of character pair tuples
	    # go through each tuple, converting them to ASCII code (ord)
	    # perform exclusive or on the ASCII code
	    # then convert the result back to ASCII (chr)
	    # merge the resulting array of characters as a string
		return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

c16 = challenge16()
helper = helper_cls()
enc= c16.enc_userinput("A"*32)
print enc.encode('hex')
enc= enc[:32] + helper.sxor("A"*16, ";admin=true;1234")+ enc[48:]
print enc.encode('hex')

#print c16.decrypt(enc[:32])
#print c16.decrypt(enc)[32:48]
print c16.decrypt(enc)[48:64]
#print c16.decrypt(enc)[64:]


#print c16.is_admin(c16.decrypt(enc).encode('hex'))
#print c16.is_admin(c16.decrypt(enc2).encode('hex'))
#print c16.decrypt()