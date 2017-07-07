import sys

plain_text = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = "ICE"

pt_bytes = bytearray()
k_bytes = bytearray()

pt_bytes.extend(plain_text)
k_bytes.extend(key)

for i in range(0, len(pt_bytes)):
	if i == 0:
		sys.stdout.write(hex(pt_bytes[i] ^ k_bytes[i]).replace("0x",""))
	else:
		sys.stdout.write(hex(pt_bytes[i] ^ k_bytes[i%3]).replace("0x",""))

	