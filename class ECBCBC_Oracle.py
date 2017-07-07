from Crypto import Random

class ECBCBC_Oracle:
	def __init__(self,random):
		self.rnd = random

	def gen_AES_key(self, size):
		return self.rnd.read(size)

print ECBCBC_Oracle(Random.new()).gen_AES_key(16)