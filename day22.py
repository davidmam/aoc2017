# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 07:49:36 2017

@author: David
"""

# day22

grid = [x.strip() for x in open('input22.txt').readlines()]

testgrid = ['..#','#..','...']
#grid=testgrid
startwidth = len(grid[0])
startheight= len(grid)

startpos = [(startheight-1)//2,(startwidth-1)//2]
startdir = 0
dirs = ((-1,0),(0,1),(1,0),(0,-1))
maxrow=maxcol=0
minrow= startheight
mincol = startwidth
visited = {}
infected = 0

def dostep ():
    '''If the current node is infected, it turns to its right. Otherwise, it turns to its left. (Turning is done in-place; the current node does not change.)
If the current node is clean, it becomes infected. Otherwise, it becomes cleaned. (This is done after the node is considered for the purposes of changing direction.)
The virus carrier moves forward one node in the direction it is facing.'''
    global startpos, startdir, visited,minrow, mincol, maxrow, maxcol
    dirchange = {'.':3,'#':1, 'W':0,'F':2}
    states = {'.':'W', 'W':'#', '#':'F', 'F':'.'}
    # states = {'.':'#', '#':'.'} # uncomment for part 1
    poskey = '{},{}'.format(startpos[0],startpos[1])
    cell = '.' #uninfected - default for new cells
    if poskey in visited: # have we already been here?
        cell=visited[poskey]
    elif startpos[0] >= 0 and startpos[0]<startheight and startpos[1] >= 0 and startpos[1]<startwidth: # if not, are we on the grid?
        cell = grid[startpos[0]][startpos[1]]
    startdir = (startdir + dirchange[cell])%4 #turn
    cell = states[cell]
    visited[poskey]=cell # save current state
    startpos[0]+=dirs[startdir][0] #move on in direction.
    startpos[1]+=dirs[startdir][1]
    if minrow > startpos[0]:
        minrow=startpos[0]
    if mincol > startpos[1]:
        mincol=startpos[1]
    if maxrow < startpos[0]:
        maxrow=startpos[0]
    if maxcol < startpos[1]:
        maxcol=startpos[1]
    return cell.count('#')

part = 10000000 #part2
# part = 10000  #part1
        
for i in range(part):
    infected += dostep()

print(infected)    
        


