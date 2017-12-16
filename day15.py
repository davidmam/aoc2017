# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 22:12:28 2017

@author: David
"""

# Day 15

'''Generator A starts with 116
Generator B starts with 299'''

starta = 116
startb = 299

factora = 16807
factorb = 48271
divisor = 2147483647

matches = 0
gena=starta
genb=startb
for n in range(40000000):
    gena = factora*gena % divisor
    genb = factorb*genb % divisor
    if ( gena & (2**16-1) )^ (genb & (2**16-1)) == 0:
        matches +=1
        
print(matches)
#part 2
multa = 4
multb = 8


matches = 0
gena=starta
genb=startb
for n in range(5000000):
    gena = factora*gena % divisor
    while (gena & (multa-1)):
        gena = factora*gena % divisor
        
    genb = factorb*genb % divisor
    while (genb & (multb-1)):
        genb = factorb*genb % divisor
    if ( gena & (2**16-1) )^ (genb & (2**16-1)) == 0:
        matches +=1
        
print(matches)