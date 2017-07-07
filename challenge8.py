import requests
import base64
from Crypto.Cipher import AES

url = "http://cryptopals.com/static/challenge-data/8.txt"
file = requests.get(url)
BLOCKSIZE=16

for line in file:
	blocks = len(line) / BLOCKSIZE
	for i in range(0,blocks):
		for a in range(0,blocks):
			if a != i and line[i*BLOCKSIZE:(i+1)*BLOCKSIZE] == line[a*BLOCKSIZE:(a+1)*BLOCKSIZE]:
				print line + " : " + line[i*BLOCKSIZE:(i+1)*BLOCKSIZE] + " == " + line[a*BLOCKSIZE:(a+1)*BLOCKSIZE]

