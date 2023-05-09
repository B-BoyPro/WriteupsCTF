#!/usr/bin/env python3

import os 
import subprocess

hint = [
  0.9994088125992486,
  0.8258436683972712,
  0.9529505815730472,
  0.08190908488360704,
  0.549252440965251
]

arr = []

for k in hint:
	arr.append(int(k*10**16))

string = ""

for x in arr:
	string +=str(x)+"\n"
stringa = string[:-1]

shell = "echo '"+stringa+"' | tac | python3 solve.py --multiple "+str(10**16)+" --lead 1"
exec_shell = os.popen(shell)

gen_cod = exec_shell.read()[:-1]

shell2 = "python3 solve.py --multiple "+str(10**16)+" --gen "+gen_cod+",20"

exec_shell2 =os.popen(shell2)
c = exec_shell2.read().split()
print("Next value of generetor : ",c[0])
