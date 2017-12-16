# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 09:07:37 2017

@author: David
"""

# Day 16

def spin (crew, number):
    s = len(crew)-number
    newcrew = crew[s:]+crew[:s]
    return newcrew

def exch (crew, a, b):
    ia = crew.index(a)
    ib = crew.index(b)
    return swap(crew, ia, ib)

def swap (crew, a, b):
    t = crew[a]
    crew[a] = crew[b]
    crew[b] = t
    return crew

data = open('input16.txt').read().strip().split(',')

dancerstart = ['a','b','c','d','e','f','g','h',
           'i','j','k','l','m','n','o','p']
dancers = dancerstart[:]

# does the dance get back to a previously seen position? 
# If so then we can use that to find how many steps to take.

seen = []
while ''.join(dancers) not in seen:
    seen.append("".join(dancers))
    for d in data:
        command = d[0]
        values = d[1:].split('/')
        if command == 's':
            dancers = spin(dancers, int(values[0]))
        elif command == 'x':
            dancers = swap(dancers,int(values[0]), int(values[1]))
        elif command =='p':
            dancers= exch(dancers, values[0], values[1])
cycles= len(seen)
part1answer = seen[1]
print(part1answer)
final = seen[1000000000%cycles]
print(final)