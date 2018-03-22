#!/usr/bin/env python3
# ECB wrapper skeleton file for 50.020 Security
# Oka, SUTD, 2014
from present import *
import argparse
import binascii

nokeybits=80
blocksize=64


def ecb(infile,outfile,key,mode):
    inp_file = open(infile, mode = 'rb')
    key_file = open(key, mode = 'r')
    out_file = open(outfile, mode = 'wb')
    print('     Openning files...')
    key = int(key_file.read(), 16)
    out = []
    if mode == 'e':
        print('     Encrypting <' + infile + '> into <' + outfile + '>...')
    elif mode == 'd':
        print('     Decrypting <' + infile + '> into <' + outfile + '>...')
    else:
        return

    plainBlock = inp_file.read(8)
    while (plainBlock != b''):
        block = ''
        for j in plainBlock:
            block += format(j, '08b')
        block = int(block, 2)

        if mode == 'e':
            out.append(binascii.unhexlify('%016x' % present(block, key)))
        elif mode == 'd':
            out.append(binascii.unhexlify('%016x' % present_inv(block, key)))

        plainBlock = inp_file.read(8)

    for byte in out:
        out_file.write(byte)
    print('-----DONE-----')

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
    mode=args.mode

    ecb(infile, outfile, keyfile, mode)


