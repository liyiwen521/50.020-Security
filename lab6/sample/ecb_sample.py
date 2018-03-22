#!/usr/bin/env python3
# ECB wrapper skeleton file for 50.020 Security
# Oka, SUTD, 2014
from present import *
import argparse
import binascii

nokeybits=80
blocksize=64


def ecb(infile,outfile,key,mode):
    i = open(infile, 'rb')
	
    #key file should only be a 1 line hex value, for example 0xFFFFFFFFFFFFFFFFFFFF or 0x00000000000000000000
    kf = open(key, 'r')
    k = kf.read()
    kf.close()
    k = int(k, 16)
	
    output_array = []
    try:
        plaintext = i.read(8)
        while plaintext != b'':
            block = ''
            for j in plaintext:
                block += format(j, "08b")
            block = int(block, 2)
            if mode == "e":
                ciphertext = present(block, k)
            elif mode == "d":
                ciphertext = present_inv(block, k)
				
            output_array.append(binascii.unhexlify('%016x' % ciphertext))
            plaintext = i.read(8)
    finally:
        i.close()
		
    o = open(outfile, 'wb')
    for j in output_array:
        o.write(j)
    o.close()
    

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Block cipher using ECB mode.')
    parser.add_argument('-i', dest='infile',help='input file')
    parser.add_argument('-o', dest='outfile',help='output file')
    parser.add_argument('-k', dest='keyfile',help='key file')
    parser.add_argument('-m', dest='mode',help='mode')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    keyfile=args.keyfile
    mode = args.mode
    ecb(infile, outfile, keyfile, mode)



