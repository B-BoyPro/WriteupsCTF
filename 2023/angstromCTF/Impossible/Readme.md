# The challenge

Let’s take a look of this challenge:

```python
def fake_psi(a, b):
    return [i for i in a if i in b]

def zero_encoding(x, n):
    ret = []

    for i in range(n):
        if (x & 1) == 0:
            ret.append(x | 1)
        x >>= 1
    return ret

def one_encoding(x, n):
    ret = []

    for i in range(n):
        if x & 1:
            ret.append(x)
        x >>= 1
    return ret

print("Supply positive x and y such that x < y and x > y.")
x = int(input("x: "))
y = int(input("y: "))

if len(fake_psi(one_encoding(x, 64), zero_encoding(y, 64))) == 0 and x > y and x > 0 and y > 0:
    print(open("flag.txt").read())
```

We see that we should provide two input and there are 2 method that will be run, if we print out these array we can see something interesting:

```python
x = 32994949
[32994949, 8248737, 257773, 64443, 32221, 8055, 4027, 2013, 503, 251, 125, 31, 15, 7, 3, 1]
y = 773233
[773233, 386617, 193309, 96655, 6041, 3021, 1511, 189, 95, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
```

after that we have another method called **fake_psi** that confront 2 array and return the common of these two, so we can put x = 1 << 64 and y = 1 to bypass the if and here is the flag: **actf{se3ms_pretty_p0ssible_t0_m3_7623fb7e33577b8a}**
