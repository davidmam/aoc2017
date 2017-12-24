# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 13:08:56 2017

@author: David
"""

class Node():
    def __init__(self, low, high):
        self.nodes=[low, high]
        self.visited = False
        
    def visitNode(self, inward):
        if inward not in self.nodes:
            raise Exception('Illegal move')
        self.visited = True
        return self.nodes[(self.nodes.index(inward)+1)%2]
    def score(self):
        return sum(self.nodes)
nodes = {}

for p in open('input24.txt').readlines():
    (low,high) = p.strip().split('/')
    n = Node(int(low), int(high))
    if int(low) in nodes:
        nodes[int(low)].append(n)
    else:
        nodes[int(low)]=[n]
    if int(high) in nodes:
        nodes[int(high)].append(n)
    else:
        nodes[int(high)]=[n]
    
def walknodes(pins,visited=[]):
    # score = [[sum([x.score() for x in visited])], len(visited)] #part 2
    score = sum([x.score() for x in visited]) #part 1
    for p in nodes[pins]:
        if p not in visited:
             pathscore = walknodes(p.visitNode(pins),visited+[p])
             #part 1
             if pathscore > score:
                 score = pathscore 
             #part 2
             #if pathscore[1] > score[1]:
             #    score = pathscore
             #elif pathscore[1] == score[1]:
             #    score[0] += pathscore[0]
                 
    return score
            
bridges = walknodes(0)
print(max(bridges[0]))