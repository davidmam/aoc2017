# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 07:11:21 2017

@author: David
"""
# Day 4
fh = open('input4.txt')
total=0
lines=0
for line in fh.readlines():
    #pw =  line.strip().split() # part 1
    pw = [''.join(sorted(x)) for x in line.strip().split()] # part 2
    lines = lines+1
    if len(pw) == len(set(pw)):
        total +=1

print(lines, total)

# Day 5
fh = open('input5.txt')

instr = [int(x) for x in fh.readlines()]
steps = 0
pos = 0
while pos < len(instr) and pos > -1:
    steps += 1
    newpos = pos + instr[pos]
    if instr[pos]>2:
        instr[pos] -= 1
    else:    
        instr[pos] +=1
    pos = newpos

print(steps)

# Day 6

data= [int(x) for x in '4	10	4	1	8	4	9	14	5	1	14	15	0	15	3	5'.split()]
hashes = {}
steps = 0
hf = ':'.join([str(x) for x in data])
while hf not in hashes:
    hashes[hf]=steps
    steps += 1    
    maxblock = data.index(max(data))
    redvalue=data[maxblock]
    data[maxblock]=0
    for r in range(1, 1+redvalue):
        data[(maxblock+r)%len(data)] += 1
    hf = ':'.join([str(x) for x in data])
    
print(steps-hashes[hf]+1)


# Day 7

nodes={}

fh = open('input7.txt')
for line in fh.readlines():
    f = line.strip().split()
    node = f[0]
    mass = int(f[1][1:-1])
    nodes[node] = nodes.get(node,{})
    nodes[node]['mass'] = mass
    if len(f)> 2:
        child = [c.replace(',','') for c in f[3:]]
        nodes[node]['children']= child
        for c in child:
            nodes[c] = nodes.get(c, {})
            nodes[c]['parent'] = node

n = list(nodes.keys())[0]
while nodes[n].get('parent', None ) != None:
    n = nodes[n]['parent']
    
print(n)
headnode=n

orders = {}
for n in nodes.keys():
    o = len(nodes[n].get('children',[]))
    orders[o]= orders.get(o,0)+1
print(orders)
        
def get_mass(n):
    childmasses = []
    kinder = nodes[n].get('children', [])
    for k in kinder:
        childmasses.append(get_mass(k))
    if  len(set(childmasses)) == 2:
        for k in kinder:
            print(n, k, nodes[k]['nodemass'], nodes[k]['mass'])        
    cm = 0
    if len(childmasses)>0:
        cm = sum(childmasses)
    nodes[n]['nodemass'] = cm+nodes[n]['mass']
    return nodes[n]['nodemass']
    
get_mass(headnode)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    