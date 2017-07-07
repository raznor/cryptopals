import pprint

def pkcs7padding(input, blocksize):
	padding = (blocksize - (len(input) % blocksize)) * str(blocksize - (len(input) % blocksize))
	if not len(padding) == 8:
		input += padding
	return input

inp = "YELLOW SUBMARINE"
bsize = 8

res = pkcs7padding(inp,bsize)
print res