# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 08:13:07 2017

@author: David
"""

# Day 12

# This is an undirected graph. Build this as a list of nodes, each node keeps a list of neighbours

nodes = {}

with open('input12.txt') as fh:
    for l in fh.readlines():
        (first, last) = l.strip().split(' <-> ')
        tojoin = last.split(', ')
        fn = nodes.get(int(first), [])
        nodes[int(first)]=fn
        for n in tojoin:
            fn.append(int(n))
            ln = nodes.get(int(n),[])
            ln.append(int(first))
            nodes[int(n)]=ln
    
def walknode(id, seen):
    node = nodes[id]
    for n in set(node):
        if n not in seen:
            seen[n]=1
            walknode(n,seen)
            
seen = {}
walknode(0, seen)
print(len(seen))

# part2

groups = 0

while len(nodes) >0:
    seen={}
    groups +=1
    start = list(nodes.keys())[0]
    print(start)
    walknode(start, seen)
    for k in seen.keys(): # remove the group from the seen list
        del nodes[k]
        
print(groups)
