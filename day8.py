# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 07:13:33 2017

@author: David
"""

registers={}

def inc (r, val):
    registers[r] = registers.get(r, 0) + val

def gt(x,y):
    return bool(x > y)

def gte(x,y):
    return bool(x >= y)

def lt(x,y):
    return bool(x < y)

def lte(x,y):
    return bool(x <= y)

def eq(x,y):
    return bool(x == y)

def neq(x,y):
    return bool(x != y)


def condition( v, plus, change,  r, symbol, value):
    registers[r] = registers.get(r, 0)
    funcs = {'>': gt,
             '<': lt,
             '>=': gte,
             '<=': lte,
             '==': eq,
             '!=': neq}
    if funcs[symbol](registers[r],value):
        if plus == 'inc':
            registers[v] = registers.get(v,0)+ change
        else:
            registers[v] = registers.get(v,0)- change
    else:
        registers[v] = registers.get(v,0)
        
maxval = 0
with open('input8.txt') as fh:
   for line in fh.readlines():
       instr = line.split()
       instr[2]= int(instr[2])
       instr[6]=int(instr[6])
       condition(instr[0],instr[1], instr[2], instr[4], instr[5],instr[6])
       if registers.get(instr[0],0) > maxval:
           maxval = registers[instr[0]]
       
print(maxval)