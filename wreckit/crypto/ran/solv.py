#!/usr/bin/env python3
from Crypto.Util.number import *
import random
from math import gcd
from pwn import *

base = 64

def enc1():
    pl = random.getrandbits(base)
    p,q = getPrime(base), getPrime(base)
    e = 0x10001
    assert gcd(e, p*q)==1
    return [pow(pl,e,p*q), p*q]

def enc2():
    pl = random.getrandbits(base)   
    p = getPrime(base*16)
    q = p+2
    while(isPrime(q)==0):
        q+=((base//32)^0x1-1)
    e = 0x10001
    assert gcd(e, p*q)==1
    return [pow(pl,e,p*q), p*q]

def enc3():
    pl = random.getrandbits(base)   
    p = getPrime(base*16)
    q = getPrime(base*16)
    e = 0x10001
    assert gcd(e, p*q)==1
    return [pow(pl,e^0x1000e,p*q), p*q]

def enc4():
    pl = random.getrandbits(base)  
    p = getPrime(base*16)
    q = getPrime(base//16)
    e = 0x10001
    assert gcd(e, p*q)==1
    return [pow(pl,e,p*q), p*q]

def decrypt(ct, n):
    p = gcd(n, pow(2, base) - 2)
    q = n // p
    phi = (p-1)*(q-1)
    d = inverse(0x10001, phi)
    return long_to_bytes(pow(ct, d, n))

conn = remote('167.71.207.218', 50611)
#167.71.207.218 50611
while True:
    menu = conn.recvuntil(b'YOU WANT what MENUS? :').decode()
    print(menu, end='')
    if 'flag' in menu:
        p = random.getrandbits(512)
        q = random.getrandbits(512)
        if p % 2 == 0: p += 1
        if q % 2 == 0: q += 1
        while not isPrime(q):
            q += ((base//32) ^ 0x1 - 1)
        while not isPrime(p):
            p += ((base//32) ^ 0x1 - 1)
        e = 0x10001
        assert gcd(e, p*q) == 1
        enc = pow(bytes_to_long(flag), e, p*q)
        conn.sendline(str(enc).encode())
    else:
        rand = random.getrandbits(32)
        ct, n = None, None
        if rand % 4 == 0:
            ct, n = enc1()
        elif rand % 4 == 1:
            ct, n = enc2()
        elif rand % 4 == 2:
            ct, n = enc3()
        elif rand % 4 == 3:
            ct, n = enc4()
        print(f'Encryption id #{rand//4 + 1}')
        print(f'ct = {ct}')
        print(f'n = {n}')
        conn.sendline(str(ct).encode())
        conn.sendline(str(n).encode())
    try:
        resp = conn.recvline(timeout=2).decode().strip()
        if 'decrypted' in resp:
            pt = int(resp.split(' = ')[-1])
            print(f'decrypted = {pt}')
        else:
