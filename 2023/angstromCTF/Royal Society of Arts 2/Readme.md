# The Challenge

Let’s take a look at the code:

```python
c = int(input("Text to decrypt: "))

if c == m or b"actf{" in long_to_bytes(pow(c, d, n)):
    print("No flag for you!")
    exit(1)

print("m =", pow(c, d, n))
```

we see that we should provide a ciphertext to decrypt, what we cannot give is if:

- The ciphertext is equal to plaintext
- After the decryption it equals to the flag

With some research on the internet we can find that if we elevate the ciphertext with an arbitrary number and let’s decrypt it, we were able to calculate the flag. 

The proof:

$$
C = m^e mod\ n
$$

$$
C' = C*2^e mod\ n
$$

if we send C’ to the decryption we would able to have m*2 then we divide by 2 and we got the flag

$$
M*2 = m^emod\ n\ *\ 2^emod\ n
$$
