def char2ahex(src):
    src = hex(ord(src))[2:]
    res = ''
    for c in src:
        o = ord(c)
        res += chr(o + (49 if o < 97 else 10))
    return res

def ahex2char(src):
    res = ''
    for c in src:
        o = ord(c)
        if o > 112:
            continue
        res += chr(o - (49 if o < 107 else 10))
    return chr(int(res, 16))

def enc(plain):
    res = ''
    for c in plain:
        res += char2ahex(c)
    return res

def dec(src):
    res = ''
    i = 0
    while i < len(src):
        res += ahex2char(src[i:i+2])
        i += 2
    return res
