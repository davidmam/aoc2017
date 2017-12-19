# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 07:30:23 2017

@author: David
"""

dirs = ((1,0),(0,1),(-1,0), (0,-1))
currdir = 0
grid = [x for x in open('input19.txt').readlines()]
moves = ['|','-']
currpos = [0,grid[0].find('|')]

visited ={}
route = ''
steps=0
currchr = grid[currpos[0]][currpos[1]]
while currchr != ' ':
    if currchr == '+':
        newdir = False
        for testdir in  [(currdir +1 )%4, (currdir +3 )%4]: 
            testchr = grid[currpos[0]+dirs[testdir][0]][currpos[1]+dirs[testdir][1]]
            if visited.get('{},{}'.format(currpos[0]+dirs[testdir][0],currpos[1]+dirs[testdir][1]), None) is not None:
                pass
            elif newdir:
                pass
            elif currpos[0]+dirs[testdir][0] <0 or currpos[1]+dirs[testdir][1] <0:
                pass
            elif currpos[0]+dirs[testdir][0] == len(grid) or currpos[1]+dirs[testdir][1] == len(grid[currpos[0]]):
                pass
            elif testchr == moves[testdir%2]:
                currdir = testdir
                newdir = True
            elif testchr == ' ':
                pass
            elif testchr not in ('+','-','|'): #test a letter 
                if grid[currpos[0]+dirs[testdir][0]+currdir[0]][currpos[1]+dirs[testdir][1]+currdir[1]]!=moves[currdir%2] and \
                grid[currpos[0]+dirs[testdir][0]-currdir[0]][currpos[1]+dirs[testdir][1]-currdir[1]]!=moves[currdir%2] :
                    # it should be a letter not on another path
                    currdir = testdir
                    newdir = True
            else: # test character is either wrong orientation or +, both of which are feasible.
                # though looking at the input, there is always at least one direction character after a +
                # so this will never get called.
                print('currently at {}, {}'.format(currpos[0], currpos[1]))
                print('direction is {}, {}'.format(currdir[0], currdir[1]))
                for a in range(max(0, currpos[0]-3), min(len(grid), currpos[1]+4)):
                    print(grid[a][max(0, currpos[1]-3):min(len(grid[a]),currpos[1]+4)])
                currdir = int(input('Enter new direction (S=0,E=1,N=2,W=3)'))
                newdir = True
        if newdir == False:
            # cannot find a way out
            print('current pos {} direction {}'.format(currpos, currdir))
            input('???')
    elif currchr not in moves:
        route += currchr
    currpos[0] += dirs[currdir][0]
    currpos[1] += dirs[currdir][1]
    steps +=1
    try:
        currchr = grid[currpos[0]][currpos[1]]
    except Exception as e: 
        print(currpos, e)

print(route, steps)           
                    
                    
                    
                    
                    
                    