# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 15:15:43 2017

@author: David
"""

# Day 25

'''Begin in state A.
Perform a diagnostic checksum after 12656374 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state C.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state D.

In state C:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state D.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state C.

In state D:
  If the current value is 0:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state E.

In state E:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state C.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state F.

In state F:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state E.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
'''

# state is value to write. Spaces to move (+ve is right), new state
states = {'A':[[1,1,'B'],[0,-1,'C']],
          'B':[[1,-1,'A'],[1,-1,'D']],
          'C':[[1,1,'D'],[0,1,'C']],
          'D':[[0,-1,'B'],[0,1,'E']],
          'E':[[1,1,'C'],[1,-1,'F']],
          'F':[[1,-1,'E'],[1,1,'A']]}

currpos = 0
currstate = 'A'
positions = {}

checksumafter = 12656374
for s in range(checksumafter):
    ns =  positions.get(currpos, 0)
    positions[currpos]= states[currstate][ns][0]
    currpos += states[currstate][ns][1]
    currstate = states[currstate][ns][2]
    
print(len([x for x in positions if positions[x]])) 