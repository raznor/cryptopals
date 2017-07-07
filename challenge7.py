from Crypto.Cipher import AES
import base64

key = b'YELLOW SUBMARINE'
filename="ciphered_file.enc"
cipher = AES.new(key)


with open(filename) as file:
			print str(cipher.decrypt(base64.b64decode(file.read())))
