#!/usr/bin/env python
# coding: utf-8

# In[ ]:


with open('data/dec4Input.txt') as d:
    input = d.read().splitlines()
#print(input)


# In[ ]:


total = 0
for i in input:
    split = i.split(',')
    elf1 = split[0]
    elf2 = split[1]
    first = []
    second = []
    firstStart = int(elf1.split('-')[0])
    firstEnd = int(elf1.split('-')[1]) + 1
    secondStart = int(elf2.split('-')[0])
    secondEnd = int(elf2.split('-')[1]) + 1
    for f in range(firstStart,firstEnd):
        first.append(f)
    for s in range(secondStart,secondEnd):
        second.append(s)
    if all(item in first for item in second) == True:
        total += 1
    elif all(item in second for item in first) == True:
        total += 1
    else:
        pass
print(total)


# In[ ]:


# part2
with open('data/dec4Example.txt') as d:
    input2 = d.read().splitlines()
print(input2)


# In[ ]:


total2 = 0
for i in input:
    split = i.split(',')
    elf1 = split[0]
    elf2 = split[1]
    first = []
    second = []
    firstStart = int(elf1.split('-')[0])
    firstEnd = int(elf1.split('-')[1]) + 1
    secondStart = int(elf2.split('-')[0])
    secondEnd = int(elf2.split('-')[1]) + 1
    for f in range(firstStart,firstEnd):
        first.append(f)
    for s in range(secondStart,secondEnd):
        second.append(s)
    for f in first:
        if f in second:
            total2 += 1
            break
print(total2)

