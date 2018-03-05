import sys
import argparse
import string

def CheckKey(key):
	try:
		k=int(key)
		if k > 0 and k < 255:
			return True
	except ValueError:
		pass
	print('Key must be an integer between 1 and', 255)
	return False

def CheckMode(mode):
	if mode.lower()=='e' or mode.lower()=='d':
		return True
	print('Mode must be either "e" or "d"')
	return False

def CheckArguments(filein, fileout, key, mode):
	if CheckKey(key) and CheckMode(mode):
		return True
	return False

def ShiftCipher(filein, fileout, key, mode):
	with open(filein, mode='rb') as fin:
		inbyte=bytearray(fin.read())
	outbyte=bytearray()
	# out=''
	if mode.lower()=='e':
		for i in inbyte:
			outbyte.append((i+key)%256)
			# out+=((i+256-key)%256).decode('utf-8')
	else:
		for i in inbyte:
			outbyte.append((i+256-key)%256)
			# out+=((i+256-key)%256).decode('utf-8')

	fout=open(fileout, mode='wb')
	fout.write(outbyte)
	return True



if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', dest='filein',help='input file')
	parser.add_argument('-o', dest='fileout', help='output file')
	parser.add_argument('-k', dest='key', help='key')
	parser.add_argument('-m', dest='mode', help='mode')

	args=parser.parse_args()
	filein=args.filein
	fileout=args.fileout
	key=args.key
	mode=args.mode

	if CheckArguments(filein, fileout, key, mode):
		print('Valid input.')
		ShiftCipher(filein, fileout, int(key), mode)
