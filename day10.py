# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 07:18:41 2017

@author: David
"""

# part 1
myinput = '230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167'
inputdata = [int(x) for x in myinput.split(',')]

mycodes = [ int(x) for x in list(range(256))]

skip = 0
def dohash(pos, length, codes):
    '''This will work on a pseudo rotating buffer'''
    # duplicate codes if pos+length > len(codes)
    codelen=len(codes)
    if pos+length >codelen:
        codes = codes+codes    
    newcodes = codes[:pos]+codes[pos:pos+length][::-1]+codes[pos+length:]
    if len(newcodes) >codelen:
        return newcodes[codelen:codelen+pos]+newcodes[pos:codelen]
    else:
        return newcodes
    
pos = 0
for p in inputdata:
    mycodes = dohash(pos, p, mycodes)
    pos += skip + p
    pos = pos % len(mycodes)
    skip +=1

print(mycodes[0]*mycodes[1])

#Part 2
#reset the input data
newinputdata = [ord(x) for x in myinput] +[17, 31, 73, 47, 23]

mycodes = [ int(x) for x in list(range(256))]
skip=0
pos=0
# 64 cycles
for r in range(64):
    for p in newinputdata:
        mycodes = dohash(pos, p, mycodes)
        pos += skip + p
        pos = pos % len(mycodes)
        skip +=1
# calculate dense hash
for x in range(0,256,16):
    k = mycodes[x] ^ mycodes[x+1]
    for  b in range(2,16):
        k = k ^ mycodes[x+b]
    hs = '0'+ hex(k)[2:]
    print(hs[-2:], sep='', end='')
print()
