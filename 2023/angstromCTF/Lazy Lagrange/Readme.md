# The challenge

The description of the challenge is : ```Lagrange has gotten lazy, but he's still using Lagrange interpolation...or is he?``` so i searched on the internet what is [**lagrange interpolation**](https://en.wikipedia.org/wiki/Lagrange_polynomial) to understand better what am i dealing with. 

Let’s take a look what they give to us

```python
#!/usr/local/bin/python
import random
with open('flag.txt', 'r') as f:
	FLAG = f.read()

assert all(c.isascii() and c.isprintable() for c in FLAG), 'Malformed flag'
N = len(FLAG)
assert N <= 18, 'I\'m too lazy to store a flag that long.'
p = None
a = None
M = (1 << 127) - 1

def query1(s):
	if len(s) > 100:
		return 'I\'m too lazy to read a query that long.'
	x = s.split()
	if len(x) > 10:
		return 'I\'m too lazy to process that many inputs.'
	if any(not x_i.isdecimal() for x_i in x):
		return 'I\'m too lazy to decipher strange inputs.'
	x = (int(x_i) for x_i in x)
	global p, a
	p = random.sample(range(N), k=N)
	a = [ord(FLAG[p[i]]) for i in range(N)]
	res = ''
	for x_i in x:
		res += f'{sum(a[j] * x_i ** j for j in range(N)) % M}\n'
	return res

query1('0')

def query2(s):
	if len(s) > 100:
		return 'I\'m too lazy to read a query that long.'
	x = s.split()
	if any(not x_i.isdecimal() for x_i in x):
		return 'I\'m too lazy to decipher strange inputs.'
	x = [int(x_i) for x_i in x]
	while len(x) < N:
		x.append(0)
	z = 1
	for i in range(N):
		z *= not x[i] - a[i]
	return ' '.join(str(p_i * z) for p_i in p)

while True:
	try:
		choice = int(input(": "))
		assert 1 <= choice <= 2
		match choice:
			case 1:
				print(query1(input("\t> ")))
			case 2:
				print(query2(input("\t> ")))
	except Exception as e:
		print("Bad input, exiting", e)
		break
```

The 18 characters of the flag ($a_0,a_1,a_2,...,a_{16},a_{17}$) are used as coefficients of a 17 degree polynomial like this:

$$
a_0+a_1x+a_2x^2+a_3x^3+a_4x^4+...+a_{16}x^{16}+a_{17}x^{17}
$$

We can write output of **************query1************** into a mathematical formula:

$$
\sum_{i=0}^{17} a[i]x^i
$$

where in the array **a** contain the characters of the flag. With some matematical intuition i solved it with GCD.

## The approch

The idea is to use divise and the GCD to take off all the characters in the array **a**. So i give to **************query1************** many integers that they GCD of two nearby element are equal to the first element → 2 4 3 9 5 25 7 49. if we group these integer in pair of 2 we can see each pairs have GCD equals to the first element. The output should be 8 integer that we put in 2 equals array:

```python
p.sendlineafter(">","2 4 3 9 5 25 7 49")

mod = []
result = []
for _ in range(8):
	number = int(p.recvline()[:-1])
	result.append(number)
	mod.append(number)
```

After that we can compute locally all the characters in **a.**

This is the script: 

```python
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
```

The idea was to cycle for every printable character and try to see if they GCD are equal, if they are we append this character to the solution and remove it from **mod**, and the new **result** should be the mod minus the next pow. After that we should find an Integer in the bound 0 to 255 multiplied by successive polynomials.

In term of mathematics:

- we use 7 and 49 to illustrate an example

$$
\sum_{i=0}^{17} a[i]7^i = k
$$

$$
\sum_{i=0}^{17} a[i]49^i = k
$$

- so we have **k** and **k’**, they surely have common a[0], and we can use GCD to find this value then after that we should remove a[0] so it becomes

$$
k = k-a[0]
$$

$$
k' = k'-a[0]
$$

- Then we should prepare the **k** and **k’** for the next cycle so what we can do is to divede **k** and **k’** for the next ****i →**** 1

$$
k = \frac k{7^1}
$$

$$
k' = \frac {k'}{49^1}
$$

- After this operation they have common a[1] and we still GCD them find the correct value

If we continue this to $i=17$ we are able to find all the characters in ****a**** and after that we give the array to the **query2** and it will give us the secret random order of the array **a** so right now we just sort it and we are able to get the flag! 

There are full [script](./solve.py)
