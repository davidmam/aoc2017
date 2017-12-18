# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 08:31:54 2017

@author: David
"""

# Day 18
# part 1
# Set up methods
import sys
registers = {}
lastsound=None
tune = []

def _snd(x):
    '''snd X plays a sound with a frequency equal to the value of X.'''
    global lastsound, registers
    f = None
    try:
        f = int(x)
    except:
        f = registers.get(x, 0)
    lastsound = f
    tune.append(f)
    return 1

def _rcv(x):    
    '''rcv X recovers the frequency of the last sound played, 
    but only when the value of X is not zero. 
    (If it is zero, the command does nothing.)'''
    try: 
        v = int(x)
    except:
        v = registers.get(x, 0)
    if v != 0:
        print('last sound {}'.format(lastsound))
        sys.exit()
    return 1

def _set(x,y):
    '''set X Y sets register X to the value of Y.'''
    global registers
    try: 
        v = int(y)
    except:
        v = registers.get(y, 0)
    registers[x] = v
    return 1
    
def _add(x,y):  
    '''add X Y increases register X by the value of Y.'''
    try: 
        v = int(y)
    except:
        v = registers.get(y, 0)
    registers[x] = registers.get(x,0) + v
    return 1


def _mul(x, y):    
    '''mul X Y sets register X to the result of multiplying the 
    value contained in register X by the value of Y.'''
    '''add X Y increases register X by the value of Y.'''
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
    try: 
        v = int(y)
    except:
        v = registers.get(y, 0)
    registers[x] = registers.get(x,0) % v
    return 1


def _jgz(x, y):        
    '''jgz X Y jumps with an offset of the value of Y, 
    but only if the value of X is greater than zero. 
    An offset of 2 skips the next instruction, 
    an offset of -1 jumps to the previous instruction, and so on.)'''
    j = 1
    try: 
        v = int(x)
    except:
        v = registers.get(x, 0)
    if v > 0:
        try:
            j = int(y)
        except:
            j = registers.get(y, 0)
    return j

def parseinstr(text):
    '''parse an instruction and call the appropriate methods'''
    functs = {'snd':_snd,
              'set':_set,
              'add':_add,
              'mul': _mul,
              'mod': _mod,
              'rcv': _rcv,
              'jgz': _jgz}
    instr = text.strip().split()
    return functs[instr[0]](*instr[1:])

commands = open('input18.txt').readlines()
pos=0

while pos <len(commands):
    pos += parseinstr(commands[pos])

# part 2

#changes:
'''Every variable is now an array of that type of variable with an index of 
the program id.
Note the program id and switch if rcv buffer is empty.
'''

pid = [0,1]
pos = [0,0]
currpid = 0
registers = [{'p':0},{'p':1}]
messages = [[],[]]
saveq = None
sent=[0,0]
lastsound=None
tune = []

def _snd(x):
    '''snd X plays a sound with a frequency equal to the value of X.'''
    global messages, currpid
    otherpid = (currpid +1)%2
    m=None
    try:
        m = int(x)
    except:
        m = registers[currpid].get(x, 0)
    messages[otherpid].append(m)
    sent[currpid] += 1
    return 1

def _rcv(x):    
    '''rcv X recovers the frequency of the last sound played, 
    but only when the value of X is not zero. 
    (If it is zero, the command does nothing.)'''
    global currpid, registers, messages, saveq
    if len(messages[currpid])> 0:
        registers[currpid][x]=messages[currpid][0]
        if len(messages[currpid])> 1:
            messages[currpid] = messages[currpid][1:]
        else:
            messages[currpid] = []
    else:
        currpid = (currpid + 1)%2
        if len(messages[currpid]) == 0:
            print('Deadlock')
            pos[currpid]=len(commands)*2
            return 0
        else:
            if saveq != None:
                registers[currpid][saveq]=messages[currpid][0]
                if len(messages[currpid])> 1:
                    messages[currpid] = messages[currpid][1:]
                else:
                    messages[currpid] = []
                saveq=x
            else:
                saveq=x
                return 0
    return 1

def _set(x,y):
    '''set X Y sets register X to the value of Y.'''
    global registers, currpid
    try: 
        v = int(y)
    except:
        v = registers[currpid].get(y, 0)
    registers[currpid][x] = v
    return 1
    
def _add(x,y):  
    '''add X Y increases register X by the value of Y.'''
    global registers, currpid
    try: 
        v = int(y)
    except:
        v = registers[currpid].get(y, 0)
    registers[currpid][x] = registers[currpid].get(x,0) + v
    return 1


def _mul(x, y):    
    '''mul X Y sets register X to the result of multiplying the 
    value contained in register X by the value of Y.'''
    '''add X Y increases register X by the value of Y.'''
    global registers, currpid
    try: 
        v = int(y)
    except:
        v = registers[currpid].get(y, 0)
    registers[currpid][x] = registers[currpid].get(x,0) * v
    return 1

def _mod(x,y):
    '''mod X Y sets register X to the remainder of dividing the value 
    contained in register X by the value of Y 
    (that is, it sets X to the result of X modulo Y).'''
    global registers, currpid
    try: 
        v = int(y)
    except:
        v = registers[currpid].get(y, 0)
    registers[currpid][x] = registers[currpid].get(x,0) % v
    return 1


def _jgz(x, y):        
    '''jgz X Y jumps with an offset of the value of Y, 
    but only if the value of X is greater than zero. 
    An offset of 2 skips the next instruction, 
    an offset of -1 jumps to the previous instruction, and so on.)'''
    global registers, currpid
    j = 1
    try: 
        v = int(x)
    except:
        v = registers[currpid].get(x, 0)
    if v > 0:
        try:
            j = int(y)
        except:
            j = registers[currpid].get(y, 0)
    return j

def parseinstr(text):
    '''parse an instruction and call the appropriate methods'''
    functs = {'snd':_snd,
              'set':_set,
              'add':_add,
              'mul': _mul,
              'mod': _mod,
              'rcv': _rcv,
              'jgz': _jgz}
    instr = text.strip().split()
    return functs[instr[0]](*instr[1:])

pos=[0,0]
currpid=0
while pos[currpid] <len(commands):
    comm = commands[pos[currpid]]
    action = parseinstr(comm)
    pos[currpid] += action
    
print(sent)