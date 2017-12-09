# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 07:40:55 2017

@author: David
"""

# Day 9

stream = open('input9.txt').read()

level = 0
garbage = False
pos =0
score = 0
size = 0
while pos < len(stream):
    if stream[pos] == '!':
        pos +=1
    elif garbage:
        if stream[pos]== '>':
            garbage = False
        else:
            size += 1
    elif stream[pos] == '<':
        garbage = True
    elif stream[pos] =='{':
        level = level+1
        score = score + level
    elif stream[pos]=='}':
        level = level -1
    pos += 1
        
print(score)
print(size)
