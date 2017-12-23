# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 07:43:15 2017

@author: David
"""
commands = [x.strip() for x in open('input23.txt').readlines()]

pos = 0
registers = {'a':1}
executions={'mul':0,'set':0,'sub':0,'mod':0,'jnz':0}
def _set(x,y):
    '''set X Y sets register X to the value of Y.'''
    global registers
    try: 
        v = int(y)
    except:
        v = registers.get(y, 0)
    registers[x] = v
    return 1
    
def _sub(x,y):  
    '''add X Y increases register X by the value of Y.'''
    global registers
    try: 
        v = int(y)
    except:
        v = registers.get(y, 0)
    registers[x] = registers.get(x,0) - v
    return 1


def _mul(x, y):    
    '''mul X Y sets register X to the result of multiplying the 
    value contained in register X by the value of Y.'''
    '''add X Y increases register X by the value of Y.'''
    global registers
    try: 
        v = int(y)
    except:
        v = registers.get(y, 0)
    registers[x] = registers.get(x,0) * v
    return 1

def _mod(x,y):
    '''mod X Y sets register X to the remainder of dividing the value 
    contained in register X by the value of Y 
    (that is, it sets X to the result of X modulo Y).'''
    global registers
    try: 
        v = int(y)
    except:
        v = registers.get(y, 0)
    registers[x] = registers.get(x,0) % v
    return 1


def _jnz(x, y):        
    '''jgz X Y jumps with an offset of the value of Y, 
    but only if the value of X is greater than zero. 
    An offset of 2 skips the next instruction, 
    an offset of -1 jumps to the previous instruction, and so on.)'''
    global registers
    j = 1
    try: 
        v = int(x)
    except:
        v = registers.get(x, 0)
    if v != 0:
        try:
            j = int(y)
        except:
            j = registers.get(y, 0)
    return j

def parseinstr(text):
    '''parse an instruction and call the appropriate methods'''
    global executions
    functs = {'set':_set,
              'sub':_sub,
              'mul': _mul,
              'mod': _mod,
              'jnz': _jnz}
    instr = text.strip().split()
    executions[instr[0]] += 1
    return functs[instr[0]](*instr[1:])
pos = 0
registers = {'a':1} # bad idea - takes too long to run
executions={'mul':0,'set':0,'sub':0,'mod':0,'jnz':0}

pos=0
while pos <len(commands):
    comm = commands[pos]
    if pos ==23:
        print(pos,comm, registers)
    action = parseinstr(comm)
    pos += action
    
print(executions['mul'])

# part 2. f is unset (and h incremented only if b is not prime.

x=0
for q in range(105700,122701,17):
    p=0
    for n in range(2,1013):
        if q%n ==0:
            p += 1
    if p:
        x += 1

print(x)



