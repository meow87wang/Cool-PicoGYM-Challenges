import zlib
import string
from itertools import product
from collections import defaultdict
import pickle
from telnetlib import Telnet
from tqdm import tqdm

def compress(text):
    return zlib.compress(bytes(text.encode("utf-8")))

def resvLength(tn, text):
    tn.write(text + b"\n")
    tn.read_until(b"\n")
    tn.read_until(b"\n")
    x = int(tn.read_until(b"\n").decode())
    return x

flag = "flag{bcde}"

print("="*20 + "Test" + "="*20)

print(flag + "flag{x:", len(compress(flag + "flag{x")))
print(flag + "flag{y:", len(compress(flag + "flag{y")))
print(flag + "flag{b:", len(compress(flag + "flag{b")))
print(flag + "flag{d:", len(compress(flag + "flag{d")))

print()

print(flag + "flag{bx:", len(compress(flag + "flag{bx")))
print(flag + "flag{by:", len(compress(flag + "flag{by")))
print(flag + "flag{bc:", len(compress(flag + "flag{bc")))

print("="*40)

charset = string.ascii_lowercase + string.ascii_uppercase +"{}_"
lengths = defaultdict(list)
flag = "picoCTF{"

for i in range(20):
    tn = Telnet('mercury.picoctf.net', 57393)
    minlength = 100000
    res = '*'
    for j in tqdm(charset):
        length = resvLength(tn,(flag + j).encode())
        if length < minlength:
            minlength = length
            res = j
    flag += res
    print(flag)
    
tn.close()
