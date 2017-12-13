# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 07:18:12 2017

@author: David
"""

# Day 13

def currpos(size, steps):
    pos = (steps) % ( 2 * (size-1))
    return pos

# build input
layers={}
with open('input13.txt') as fh:
    for line in fh.readlines():
        (l,d) = line.strip().split(': ')
        layers[int(l)] = int(d)

#part 2
sev=1
delay = 0

while sev != 0:
    sev = 0
    steps=0
    delay += 1
    while steps <= max(layers.keys()):
        if layers.get(steps, 0):
            if currpos( layers[steps],steps+delay) == 0:
                sev += steps * layers[steps]
                if steps == 0:
                    sev+=1 # to get round the multiply by zero
        steps +=1

print(delay, sev)
    
