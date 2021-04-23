import random

key = [chr(x) for x in range(65, 91)]
key += [chr(x) for x in range(97, 123)]
nt = [chr(x) for x in range(48, 58)]

def enc(plain):
    res = ''
    for c in plain:
        o = ord(c)
        if o < 10 or o > 999:
            return 'Error'
        if o >= 100:
            res += random.choice(key)
        res += str(o)
    return res

def dec(numtxt):
    res = ''
    i = 0
    while i < len(numtxt):
        if numtxt[i] not in nt:
            res += chr(int(numtxt[i+1:i+4]))
            i += 4
        else:
            res += chr(int(numtxt[i:i+2]))
            i += 2
    return res
