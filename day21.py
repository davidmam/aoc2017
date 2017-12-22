# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 08:27:24 2017

@author: David
"""

#day 21

# build rotation and reflection matrices for each operation

rot2 = [[0, 1, 2, 3],
 [3, 0, 1, 2],
 [2, 3, 0, 1],
 [1, 2, 3, 0],
 [1, 0, 3, 2],
 [0, 3, 2, 1],
 [3, 2, 1, 0],
 [2, 1, 0, 3]]

rot3 = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
 [6, 3, 0, 7, 4, 1, 8, 5, 2],
 [8, 7, 6, 5, 4, 3, 2, 1, 0],
 [2, 5, 8, 1, 4, 7, 0, 3, 6],
 [2, 1, 0, 5, 4, 3, 8, 7, 6],
 [0, 3, 6, 1, 4, 7, 2, 5, 8],
 [6, 7, 8, 3, 4, 5, 0, 1, 2],
 [8, 5, 2, 7, 4, 1, 6, 3, 0]]


def fliprot(cell, rot):
    return ''.join(str(x) for x in [cell[y] for x, y in zip(cell,rot)])

map2 = {}
map3 = {}

grid = ['.#.',
        '..#',
        '###']

for instr in open('input21.txt').readlines():
    (pat, trans) = instr.split(' => ')
    if len(pat)==5:
        map2[pat.replace('/','')]=trans.strip().split('/')
    else:
        map3[pat.replace('/','')]=trans.strip().split('/')

def expand(grid):
    newgrid = []
    if len(grid)%2 == 0:
        for r in range(0, len(grid),2):
            newgrid += ['','','']
            for c in range(0,len(grid), 2):
                pattern = grid[r][c:c+2]+grid[r+1][c:c+2]
                newpat=''
                for p in rot2:
                    if fliprot(pattern,p) in map2:
                        newpat=fliprot(pattern,p)
                        break
                if len(newpat)==0:
                    print('input is {}'.format(pattern))
                    input('???')
                newgrid[-3]+=map2[newpat][0]
                newgrid[-2]+=map2[newpat][1]
                newgrid[-1]+=map2[newpat][2]
    else:
        for r in range(0, len(grid),3):
            newgrid += ['','','','']
            for c in range(0,len(grid), 3):
                pattern = grid[r][c:c+3]+grid[r+1][c:c+3]+grid[r+2][c:c+3]
                newpat=''
                for p in rot3:
                    if fliprot(pattern,p) in map3:
                        newpat=fliprot(pattern,p)
                        break
                if len(newpat)==0:
                    print('input is {}'.format(pattern))
                    input('???')
                newgrid[-4]+=map3[newpat][0]
                newgrid[-3]+=map3[newpat][1]
                newgrid[-2]+=map3[newpat][2]
                newgrid[-1]+=map3[newpat][3]
    return newgrid
        