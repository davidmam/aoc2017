# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 08:54:56 2017

@author: David
"""
import re

# Day 20 

# long term the particle with slowest acceleration is going to be the one to keep.

particles = []

example='p=<1262,1236,601>, v=<13,-44,-43>, a=<-8,-2,1>'
entry = re.compile(r'p=<([^,]+),([^,]+),([^>]+)>, v=<([^,]+),([^,]+),([^>]+)>, a=<([^,]+),([^,]+),([^>]+)>')

minacc = 100000000
slowp = []
for p in open('input20.txt').readlines():
    particles.append([int(x) for x in entry.match(p).groups()])
    acc = sum( x**2 for x in particles[-1][6:])
    if acc < minacc:
        minacc = acc
        slowp = [len(particles)-1]
    elif minacc == acc:
        slowp.append(len(particles)-1)

print(slowp) # and pick one

# part 2
# iterate through the particles looking for colocating one.

def getpos(start):
    newpos = start[0:3]
    initv = start[3:6]
    accel = start[6:]
    for d in range(3):
        initv[d] += accel[d]
        newpos[d] += initv[d]
        
    return newpos+initv+accel

current = [x for x in range(len(particles))]
steps = 0
converge = 0 # set convergence limits.
while converge < 100000:
    collisions = []
    positions = {}
    for p in current:
        tpos = ','.join([str(x) for x in particles[p][:3]])
        if tpos in positions:
            positions[tpos].append(p)
        else:
            positions[tpos] = [p]
        particles[p] = getpos(particles[p])
    if len(current) == len(positions):
        converge +=1
    else:
        for p in [ x for x in positions if len(positions[x]) >1]:
            for n in positions[p]:
                try:
                    current.remove(n)
                except:
                    print('trying to remove {} in {} from {}'.format(n, p, current))
        print(len(current), steps)
        converge=0
    steps += 1

