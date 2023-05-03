#!/usr/bin/env python3

from pwn import *
from math import gcd
import string

caracter = string.printable

p = remote("challs.actf.co", 32100)
p.sendlineafter(": ","1")
p.sendlineafter(">","2 4 3 9 5 25 7 49")

mod = []
result = []
for _ in range(8):
	number = int(p.recvline()[:-1])
	result.append(number)
	mod.append(number)

solution = []

for j in range(18):
	for k in caracter:
		cap = ord(k)
		if gcd(result[0]-cap,result[1]-cap)%2 == 0 and gcd(result[2]-cap,result[3]-cap)%3 == 0 and gcd(result[4]-cap,result[5]-cap)%5 == 0 and gcd(result[6]-cap,result[7]-cap)%7 == 0:
			solution.append(cap);
			mod[0] = mod[0] - cap*2**j	
			mod[1] = mod[1] - cap*4**j	
			mod[2] = mod[2] - cap*3**j	
			mod[3] = mod[3] - cap*9**j	
			mod[4] = mod[4] - cap*5**j	
			mod[5] = mod[5] - cap*25**j	
			mod[6] = mod[6] - cap*7**j	
			mod[7] = mod[7] - cap*49**j	
			result[0] = mod[0] //(2**(j+1))
			result[1] = mod[1] //(4**(j+1))
			result[2] = mod[2] //(3**(j+1))
			result[3] = mod[3] //(9**(j+1))
			result[4] = mod[4] //(5**(j+1))
			result[5] = mod[5] //(25**(j+1))
			result[6] = mod[6] //(7**(j+1))
			result[7] = mod[7] //(49**(j+1))
			break;


to_send = " ".join(str(x) for x in solution)

#Query number 2
p.sendlineafter(": ","2")
p.sendlineafter(">",to_send)

shuffle = p.recvline().split()
shuffle = [int(x) for x in shuffle]

sort_arr = []

for i in range(len(shuffle)):
	sort_arr.append([shuffle[i],solution[i]])

sort_arr.sort()

flag = ""
for k,t in sort_arr:
	flag += chr(t)

print(flag)

p.close()