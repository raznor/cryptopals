class Padding_Error(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)

class challenge15:
	def __init__(self, str_with_padding):
		self.str_with_padding = str_with_padding

	def check_valid_padding(self):
		if(bytearray(self.str_with_padding[15])[0] > 0x10):
			raise Padding_Error("Padding size extends Blocksize")

		for index in range(14, 15 - bytearray(self.str_with_padding[15])[0], -1):
			if self.str_with_padding[index] != self.str_with_padding[index+1]:
				raise Padding_Error("Padding does not match")

		return bytearray(self.str_with_padding[15])[0]

	def cut_padding(self):
		return self.str_with_padding[0:16-self.check_valid_padding()]


c15 = challenge15("ICE ICE BAB\x05\x05\x05\x05\x05")
try:
	print c15.cut_padding()	
except Padding_Error as pe:
	print "not a valid padding"
