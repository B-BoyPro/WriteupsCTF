# Challenge

Let’s take a look of the main.js

```jsx
const { CURVE, Point } = require('@noble/secp256k1');
const { BigNumber } = require('ethers');
const { keccak256, arrayify, getAddress, hexDataSlice } = require('ethers/lib/utils');
const {writeFileSync} = require('fs');

(async () => {
    writeFileSync('hint.json', JSON.stringify(new Array(5).fill(true).map(Math.random), null, 2), {encoding: 'utf-8'});
    const seedKey = arrayify(BigNumber.from(keccak256(Math.floor(Math.random() * Number.MAX_SAFE_INTEGER))).add(BigNumber.from('0x260026002600260026002600').mul(0x2600n)).mod(CURVE.n));
    let newPoint = Point.fromPrivateKey(seedKey);
    
    for (let i = 1; ; i++) {
        newPoint = newPoint.add(Point.BASE);
        const newAddress = hexDataSlice(keccak256(hexDataSlice('0x' + newPoint.toHex(), 1)), 12);
        if (newAddress.startsWith('0x2600')) {
            return void writeFileSync('flag.json', JSON.stringify({
                privateKey: BigNumber.from(seedKey).add(i).toHexString(),
                publicKey: getAddress(newAddress)
            }, null, '\t\v\n\r\f'), {encoding: 'utf-8'});
        }
      }
})();
```

It seems a normal ECC generation, that save the key in the flag.json, also we have a hint.json, and the admin gives us only the hint.json, we should try to recover the flag.json then we should wrap the MD5 of this file to the flag format to obtain the correct flag.

What we can see in the hint file is only 5 number that generate by the math.random, i didn’t understand why this should be a hint for us because it’is generate with math.random and i think it’s really secure, but it isn’t, indeed after hour of searching i find a paper said that math random of the javascript is not secure for the crytography cause the attacker can predict the next number of it by having some number of the generator. 

So after that i’m doing a lot of search and i find a [youtuber](https://www.youtube.com/watch?v=_Iv6fBrcbAM&ab_channel=NathanialLattimer) that explain the vulnerability of it, also the exploit for this on the [Github](https://github.com/d0nutptr/v8_rand_buster) repository, so i copied it and run it then i found what we want: the next value of math.random.

Full script is avaible [here](./solve.py)