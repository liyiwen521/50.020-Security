#!/usr/bin/env python3
# ECB plaintext extraction skeleton file for 50.020 Security
# Oka, SUTD, 2014
import argparse
import sys
import operator

def getInfo(headerfile):
    f = open(headerfile, 'rb')
    plaintext = f.read()
    f.close()
    return plaintext

	
def frequency_analysis(infile):
    f = open(infile, 'rb')
    h = getInfo(headerfile)
    plaintext = f.read(len(h)+1)
    plaintext = f.read(8)
    d = {}
    while plaintext != b'':
        if plaintext in d:
            d[plaintext] += 1
        else:
            d[plaintext] = 1
        plaintext = f.read(8)
    s = sorted(d.items(), key=operator.itemgetter(1))
    f.close()
    return s[-1][0]

	
def extract(infile,outfile,headerfile):
    white_bytes = frequency_analysis(infile)

    input_file = open(infile, 'rb')
    output_array = []
    h = getInfo(headerfile)
    len_h = len(h)
    try:
        plaintext = input_file.read(len(h)+1)
        plaintext = input_file.read(8)
        while plaintext != b'':
            if plaintext == white_bytes:
                output_array.append('00000000')
            else:
                output_array.append('11111111')
            plaintext = input_file.read(8)
    finally:
        input_file.close()
	
    output_file = open(outfile, 'w')
    output_file.write(h.decode('utf-8') + '\n')
    for i in output_array:
        output_file.write(i)
    output_file.close()

	
if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Extract PBM pattern.')
    parser.add_argument('-i', dest='infile',help='input file, PBM encrypted format')
    parser.add_argument('-o', dest='outfile',help='output PBM file')
    parser.add_argument('-hh', dest='headerfile',help='known header file')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    headerfile=args.headerfile

    print('Reading from: %s'%infile)
    print('Reading header file from: %s'%headerfile)
    print('Writing to: %s'%outfile)

    success=extract(infile,outfile,headerfile)

            
