import sys
import argparse
import string

def CheckInput(filein):
	try:
		s=open(filein, mode='r', encoding='utf-8', newline='\n').read()
	except FileNotFoundError:
		print('Can\'t find the input file.')
		return False

	# print (s)
	for c in s:
		if c not in string.printable:
			print (c)
			return False
	return True

def CheckKey(key):
	try:
		k=int(key)
		if k > 1 and k < len(string.printable) - 1:
			return True
	except ValueError:
		pass
	print('Key must be an integer between 1 and', len(string.printable))
	return False

def CheckMode(mode):
	if mode.lower()=='e' or mode.lower()=='d':
		return True
	print('Mode must be either "e" or "d"')
	return False
def CheckArguments(filein, fileout, key, mode):
	if CheckKey(key) and CheckMode(mode) and CheckInput(filein):
		return True
	return False

def ShiftCipher(filein, fileout, key, mode):
	s=open(filein, mode='r', encoding='utf-8', newline='\n').read()
	chardict={}
	for c in string.printable:
		chardict[c]=string.printable.index(c)
	out=''
	if mode.lower()=='e':
		for c in s:
			out+=string.printable[(chardict[c]+key)%len(string.printable)]
	else:
		for c in s:
			out+=string.printable[(chardict[c]-key)]

	fout=open(fileout, mode='w', encoding='utf-8', newline='\n')
	fout.write(out)
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

