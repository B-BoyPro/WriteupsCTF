# DIY-enc

Our team l3ak got first blood on this challenge, i will explain a little bit my idea and how to approch to it 

# The Challenge

If we take a look of the challenge file we may see that it encrypts with AES_CTR, if you don’t know how it works, you can check out [wikipedia](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation) link that will explain to you. 

Basically it works on block of 16 bits and let’s assume that the encryption of this mode is using xor, so we have a key that will xor the plaintext and produce the ciphertext as it below 

$$
PT_1\ ⊕\ KEY_1 = CT_1 
$$

For every block the KEY it’s different so we can’t use any properties of  xor to attack and break this encryption.

But if we know the plaintext and the ciphertext we can retrieve the key using the inverse formula.

# Idea

We know the flag length which is 19 furthermore we know that the plaintext it’s 3 times flag, what we can do is to choise a length to give the server, it will take some random bytes of this length, encode in base 64 and using the key to encrypt this bytes.

We don’t know what bytes will be created so we can’t try use bruteforce to attack the server. With some length of plaintext the Base64 will produce ```==``` at the end , if we know the plaintext we can know also the key because if we xor the pt with the ct we have the key.

# Exploit

We should choose carefully what length to provide to the server to create a base64 with == at the end, with some try the length that we should provide is in this array  arr = [4,7,10,34,37,40] :

| **Length provided**  | **Tot length of base64 Encoded** | **position of ==** | **flag bytes we can recover** |
| --- | --- | --- | --- |
| 4 | 8  | 7,8 | 7,8 |
| 7 | 12 | 11,12 | 11,12 |
| 10 | 16 | 15,16 | 15,16 |
| 34 | 48 | 47,48 | 9,10 |
| 37 | 52 | 51,52 | 13,14 |
| 40 | 56 | 55,56 | 17,18 |

Then we just combine all of it and the flag magically appears