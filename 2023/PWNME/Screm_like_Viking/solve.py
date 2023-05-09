#!/usr/bin/env python3

from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
from Crypto.Util.Padding import pad
from pwn import *
from sympy.ntheory.modular import crt
from Crypto.Util.number import *
import math 
from gmpy2 import * 

<<<<<<< HEAD
=======
#PWNME{h4st4rd_br0adc4st_d3str0y_s1mple_p4dd1ng}

>>>>>>> 9df12aa8296763caa887ea12412eea5e39164520
n = []
pos_flag = []
for k in range(17):
	p = remote("51.68.95.78",32770)
	
	arr = []
	result = []
	for i in range(4):
		p.sendlineafter("> ","Encrypt")
		p.sendlineafter("> ",str(i))
		arr.append(bytes_to_long(pad(long_to_bytes(i), 50))**17)
		c = int(p.recvline()[:-1])
		result.append(c)

	n_poss = math.gcd(arr[0]-result[0],arr[1]-result[1],arr[2]-result[2],arr[3]-result[3])
	n.append(n_poss)
	p.sendlineafter("> ","Flag")
	p.recvuntil(b": ")
	flag = int(p.recvline()[:-1])
	pos_flag.append(flag)
	p.close()
	print(k)

print(n,pos_flag)
solution = crt(n,pos_flag)[0]
print(crt(pos_flag,n))
print(gmpy2.iroot(solution,17))
