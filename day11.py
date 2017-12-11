# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 05:55:23 2017

@author: David
"""

#Day 11

# Approach:
# COut total steps in each direction then work out manhattan distance

ifh = open('input11.txt')
data = ifh.read().strip().split(',')
steps = {'n':0, 's':0, 'nw':0, 'sw':0, 'ne':0,'se':0}
maxsteps=0

def getsteps(a): # needed for part 2
    # will be a residual count in two directions
    if a['nesw'] > 0 and a['nwse']> 0:
        s = abs(a['ns']+ max(a['nesw'],a['nwse']))
    elif a['nesw'] < 0 and a['nwse'] < 0:
        s = abs(a['ns'] - max(a['nesw'],a['nwse']) + (max(a['nesw'],a['nwse'])-min(a['nesw'],a['nwse'])))
    else:
        s = abs(a['nesw']+a['ns'])+abs(a['nwse']+a['ns'])
    return s

for k in data:
    steps[k]=steps.get(k, 0)+1
    axes = {'ns': steps['n']-steps['s'],
        'nwse': steps['nw']-steps['se'],
        'nesw': steps['ne']-steps['sw']}

    tohim = getsteps(axes)
    if tohim > maxsteps:
        maxsteps=tohim
print(steps)
#part1, part 2
print(tohim, maxsteps)




#nwse + nesw = ns
#nesw - ns = nwse
# equation is nwse + ((nesw-ns) +ns) 