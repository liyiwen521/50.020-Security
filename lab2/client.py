#!/usr/bin/python3
# -*- coding: utf-8 -*-
# DA+Nils 2018

"""
Lab2: Breaking Ciphers

Pwntool client for python3

Install: see install.sh

Documentation: https://python3-pwntools.readthedocs.io/en/latest/
"""

from pwn import remote
import string
import random
import math
# pass two bytestrings to this function
def XOR(a, b):
    r = b''
    for x, y in zip(a, b):
        r += (x ^ y).to_bytes(1, 'big')
    return r


def sol1():
    conn = remote(URL, PORT)
    message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
    conn.sendline("1")  # select challenge 1

    dontcare = conn.recvuntil(':')
    challenge = conn.recvline()
    challenge_str = challenge.decode('utf-8')
    # decrypt the challenge here
    frequencyDict = {}
    for i in challenge_str:
        if i in frequencyDict:
            frequencyDict[i] += 1
        else:
            frequencyDict[i] = 1

    for i in frequencyDict:
        frequencyDict[i] = float(frequencyDict[i]) / len(challenge_str)


    mapping=generateSubstituteKeys(frequencyDict)
    solution_str = substitute(challenge_str,mapping)
    print(solution_str)
    
    conn.send(solution_str)
    message = conn.recvline()
    message = conn.recvline()
    if b'Congratulations' in message:
        print(message)

    conn.close()

def generateSubstituteKeys(frequencyDict):
    orderedKeys=sorted(frequencyDict,key=frequencyDict.get,reverse=True)
    orderedEnglish=[' ','e','t','a','o','h','r','n','d','i','s','l','w','\n','g',',','u','c','m','y','f','p','.','b','k','v','\"','-','\'','j','q','?','\t']

    mapping = {}
    for i in range (33):
        mapping[orderedKeys[i]] = orderedEnglish[i]

    for i in range (0, len(string.printable)):
        if string.printable[i] not in mapping:
            mapping[string.printable[i]]=string.printable[i]

    return mapping

def substitute(text,mapping):
    result=''
    for i in text:
        result+=mapping[i]
    return result

def sol2():
    mask1 = XOR(b'1001704', b'1000000')
    mask2 = XOR(b'0', b'4')

    for i in range (27):
        for j in range (23, 31): # This is supposedly run from 0 to 31, however it might stop before reaching the answer
            # Optimal i = 11, j = 24
            conn = remote(URL, PORT)
            message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
            conn.sendline("2")  # select challenge 2

            dontcare = conn.recvuntil(':')
            challenge = conn.recvline()

            message = challenge[:i] + XOR(mask1, challenge[i:i+7]) + challenge[i+7:]
            message = message[:j] + XOR(mask2, challenge[j:j+1]) + message[j+1:]
            try:
                conn.send(message)
                message = conn.recvline()
                message = conn.recvline()
                if b'1001704' in message and b'grade 4' in message:
                    print('Positions of masks: ', i, j)
                    print(message)
                    conn.close()
                    return
            except EOFError:
                print('EOF Error')
            conn.close()


if __name__ == "__main__":

    # NOTE: UPPERCASE names for constants is a (nice) Python convention
    URL = 'scy-phy.net'
    PORT = 1337

    sol1()
    sol2()
