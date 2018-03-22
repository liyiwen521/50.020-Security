#!/usr/bin/env python3
# ECB plaintext extraction skeleton file for 50.020 Security
# Oka, SUTD, 2014
import argparse
import operator

def getInfo(headerfile):
    print('     Getting header file info...')
    header = open(headerfile, mode='rb').read()
    return header

def getWhiteBytes(infile, header):
    print('     Finding white byte...')
    file = open(infile, mode = 'rb')
    inp = file.read(len(header) + 1)
    inp = file.read(8)
    d = {}
    while inp != b'':
        if inp in d:
            d[inp] += 1
        else:
            d[inp] = 1
        inp = file.read(8)
    frequence = sorted(d.items(), key = operator.itemgetter(1))
    file.close()
    print('     Found white byte!')
    return frequence[-1][0]


def extract(infile,outfile,headerfile):
    print('     Extracting <' + infile + '> into <' + outfile + '>...')
    header = getInfo(headerfile)
    whiteBytes = getWhiteBytes(infile, header)

    inp_file = open(infile, mode = 'rb')
    out = []

    # skip header portion
    inp = inp_file.read(len(header) + 1)

    # start reading file
    print('     Extracting key message...')
    inp = inp_file.read(8)
    while inp != b'':
        if inp == whiteBytes:
            out.append('00000000')
        else:
            out.append('11111111')
        inp = inp_file.read(8)

    out_file = open(outfile, mode = 'w')
    out_file.write(header.decode('utf-8') + '\n')
    for byte in out:
        out_file.write(byte)

    print('-----DONE-----')

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

            
