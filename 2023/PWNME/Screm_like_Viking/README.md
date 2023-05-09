# Challenge

Description: '```Our protagonist John is in a room, he hears some kind of noise, like something resonating. But he doesn't understand it... Perhaps he could play with his own echoes to guess what the meaning of this famous resonance could be...``` 

Let’s take a look of the chall.py

```python
#!/usr/bin/env python3

from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
from Crypto.Util.Padding import pad

e = 17
p = getPrime(512)
q = getPrime(512)
N = p * q

def encrypt(m):
    assert 0 <= m < N    
    c = pow(bytes_to_long(pad(long_to_bytes(m), 50)), e, N)
    return int(c)

def encrypt_flag():
    with open("flag.txt", "rb") as f:
        flag = f.read()
    c = pow(bytes_to_long(pad(flag, 50)), e, N)
    return c

def main():
    try:
        while True:
            print("Enter your option (Encrypt or Flag) > ", end='')
            cmd = (input().strip())
            if cmd == "Encrypt":
                print("Enter your integer to encrypt > ", end='')
                m = int(input())
                c = encrypt(m)
                print(str(c) + '\n')
            elif cmd == "Flag":
                c = encrypt_flag()
                print("Flag cipher for you: " + str(c) + '\n')
                return
    except Exception as e:
        print("An error occured:\n", e)

if __name__ == "__main__":
    main()
```

We notice that e is very small = 17, we have many attack when the public exponent is small such as find the i-root of the ciphertext, but in this challenge we can’t use it because the plaintext of the FLAG has a padding to 50 length, after that the FLAG will be very long  therefore it’s not possible to use that attack.

## The approch

After searching on the internet the attack that shoul work is **Håstad's broadcast attack,** it use chinese remainder theorem to attack it, what should we have is 17 times N and 17 times the FLAG, because in this scenario we have e = 17.

<<<<<<< HEAD
In this [chall.py](./chall.py) it doesn’t print N for u, so we should recover it using GCD, so the idea is to encrypt m then calculate $m^{17}$ then subtract the ciphertext that gives to us, then we send another m and do the same approch, then we can calculate N by using GCD of them 
=======
In this [chall.py](http://chall.py) it doesn’t print N for u, so we should recover it using GCD, so the idea is to encrypt m then calculate $m^{17}$ then subtract the ciphertext that gives to us, then we send another m and do the same approch, then we can calculate N by using GCD of them 
>>>>>>> 9df12aa8296763caa887ea12412eea5e39164520

```python
import math
arr = []
result = []
for i in range(4):
	p.sendlineafter("> ","Encrypt")

	p.sendlineafter("> ",str(i))
	arr.append(bytes_to_long(pad(long_to_bytes(i), 50))**17)
	c = int(p.recvline()[:-1])
	result.append(c) 
n_poss = math.gcd(arr[0]-result[0],arr[1]-result[1],arr[2]-result[2],arr[3]-result[3])
```

I send 4 times to ensure that N will be correct, basically this is the idea, so we should open 17 times recover 17 times N and 17 times Flag and calculate the crt and we will find the $flag^{17}$ then we do the 17-root to find the Flag.

Full script are avaible [here](./solve.py)