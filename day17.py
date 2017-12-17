# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 13:25:22 2017

@author: David
"""

# Day 17

step = 386

values = [0]
pos = 0
for n in range(1,2018):
    values.insert(pos+1,n)
    pos = (pos + 1 + step) % len(values)
print(values[values.index(2017)+1])   

#part 2 - 0 is always at the beginning so you only need to check if that is the key.
# no need to keep the whole buffer.

val1 = None
pos = 0
for n in range(1,50000000):
    pos = (pos + step + 1) %n
    if pos == 0:
        val1 = n

print(val1)