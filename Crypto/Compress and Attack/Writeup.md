# Compress and Attack

## Abstract

The challenge provides an oracle that you can compress and encrypt arbitrary messages concatenated with the flag. The encryption algorithm is Salsa20 and every encryption uses a different and random secret key. The encryption seems unbreakable. In fact, this is the kind of challenge that needs not to break the cipher.

## Observations

First, notice that the oracle informs you of the length of the encrypted text. Since Salsa20 is a stream cipher, the length is equal to the plaintext.
The length of compressed text will be the key to solving the challenge.

### Compression

We only need to know one property about compression algorithms to solve the challenge.
That is, the lower the entropy of the original text, the shorter the compressed text is.

Repeated substrings can reduce the entropy and shorten the compressed text in the module "zlib" used by the challenge. The table is an example for this observation. Some have compressed length 20 because they repeat the previous text more than other same length inputs.

| input              | compressed length |
|--------------------|-------------------|
| `flag{bcde}flag{x` | 21                |
| `flag{bcde}flag{y` | 21                |
| `flag{bcde}flag{b` | 20                |
| `flag{bcde}flag{d` | 21                |
|                    |                   |
| `flag{bcde}flag{bx`| 21                |
| `flag{bcde}flag{by`| 21                |
| `flag{bcde}flag{bc`| 20                |

## Method 

By the observation, we can reveal the flag from the encrypted text length.
We know that the flag starts with `picoCTF{`, so we: 

1. Set `flag = "picoCTF{"`
2. Query all possible `"flag" + c` where `c` is any character. 
3. Find the character that generates the shortest output length among them, it is the next character of the flag.
4. Append it to the `flag` string and repeat the procedures.

<details>
  <summary>Flag</summary>
  
  `picoCTF{sheriff_you_solved_the_crime}`
  
</details>
