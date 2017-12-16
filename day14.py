# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 21:26:24 2017

@author: David
"""

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


def makehash(text):
    newinputdata = [ord(x) for x in text] +[17, 31, 73, 47, 23]
    skip=0
    pos=0 
    mycodes = [ int(x) for x in list(range(256))]
    for r in range(64):
        for p in newinputdata:
            mycodes = dohash(pos, p, mycodes)
            pos += skip + p
            pos = pos % len(mycodes)
            skip +=1
    # calculate dense hash
    binhash = ''
    for x in range(0,256,16):
        k = mycodes[x] ^ mycodes[x+1]
        for  b in range(2,16):
            k = k ^ mycodes[x+b]
        binhash += '{:08b}'.format(k)
    return binhash

hashkey='hfdlxzhv'

grid = []
for r in range(128):
    grid.append(makehash(hashkey+'-{}'.format(r)))

squares =sum([x.count('1') for x in grid])

print(squares)

#part2 

# Start at the first 1 and exhaustively search for all contiguous squares
# hash each index so you know if you have seen it yet. SHould be a max of squares in size

visited = {}

def findsquares (row,col):
    print('visiting {}, {}'.format(row,col))
    visited['{},{}'.format(row, col)] = 1
    for r in [-1,0,1]:
        for c in [-1,0,1]:
            if r+row <0 or r+row > 127 or c+col<0 or c+col > 127 or abs(c)+abs(r) != 1 :
                continue
            elif grid[row+r][col+c] == '1' and visited.get('{},{}'.format(row+r, col+c), None) is None:
                findsquares(row+r, col+c)
    
            
myrow = 0
mycol = grid[myrow].find('1', 0)
regions = 0
while myrow < 128:
    if visited.get('{},{}'.format(myrow, mycol), None) is None:
        findsquares(myrow, mycol)
        regions +=1
        print('region ',regions)
    mycol=grid[myrow].find('1',mycol+1)
    if mycol == -1:
        myrow +=1        
        mycol=grid[myrow].find('1',0)
# this wil lthrow an error when it steps off the grid.    
