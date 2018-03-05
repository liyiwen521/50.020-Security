import sys
import argparse

def readFlag(flag):
	try:
		byte=open(flag, mode='rb').read()
	except FileNotFoundError:
		print('Can\'t find the input file.')
	
	print(type(byte))
	# print(byte)
	return byte

def shiftCipher(inbyte,fileout,key):
	outbyte=bytearray()
	for i in inbyte:
		outbyte.append((i+256-key)%256)

	fout=open(fileout, mode='wb')
	fout.write(outbyte)
	return True

def decryptFlag(flag):
	flagbytes=readFlag(flag)
	for key in range (1, 256):
		name='flagout'+str(key)
		shiftCipher(flagbytes,name,key)



if __name__=="__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument('flag')
	args=parser.parse_args()
	flag=args.flag

	decryptFlag(flag)
