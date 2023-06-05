#!/usr/bin/env python3

from base64 import b64encode
from pwn import * 

arr = [4,7,10,34,37,40]

p = remote("challs.dantectf.it" ,31510)

p.recvuntil(b"flag = ")

flag = bytes.fromhex(p.recvline()[:-1].decode())
solution = []

for i in arr:
	p.sendlineafter(">",str(i))
	p.recvuntil("ct = ")

	len_b64 = len(b64encode(os.urandom(i)))
	test = bytes.fromhex(p.recvline()[:-1].decode())

	key = (xor(b"==",test[-2:]))
	solution.append(xor(key,flag[len_b64-2:len_b64]))

print(solution)

#reassemble the flag 
flag = b"DANTE{"
for i in range(3):
	flag += solution[i]+solution[i+3]
flag += b"}"
print(flag)