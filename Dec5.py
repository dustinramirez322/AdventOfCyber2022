#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#    [D]    
#[N] [C]    
#[Z] [M] [P]
# 1   2   3 


# In[ ]:


with open('data/dec5Input.txt') as d:
    input = d.read().splitlines()
#print(input)


# In[ ]:


#stack1 = [1, 'Z', 2, 'N']
#stack2 = [1, 'M', 2, 'C', 3, 'D']
#stack3 = [1, 'P']
#stack1 = ['Z', 'N']
#stack2 = ['M', 'C', 'D']
#stack3 = ['P']
stack1 = ['G', 'D', 'V', 'Z', 'J', 'S', 'B'] 
stack2 = ['Z', 'S', 'M', 'G', 'V', 'P']
stack3 = ['C', 'L', 'B', 'S', 'W', 'T', 'Q', 'F']
stack4 = ['H', 'J', 'G', 'W', 'M', 'R', 'V', 'Q']
stack5 = ['C', 'L', 'S', 'N', 'F', 'M', 'D']
stack6 = ['R', 'G', 'C', 'D']
stack7 = ['H', 'G', 'T', 'R', 'J', 'D', 'S', 'Q']
stack8 = ['P', 'F', 'V']
stack9 = ['D', 'R', 'S', 'T', 'J']


# In[ ]:


for i in input:
    test = i.split(' ')
#    print(test)


# In[ ]:


for i in input:
    move = i.split(' ')
    amount = int(move[1])
    original = int(move[3])
    new = int(move[5])
#    print(f'{amount} {original} {new}')
    stackFrom = 'stack' + str(original)
    stackTo = 'stack' + str(new)
#    print(globals()[stackFrom])
    x = 0
    while x < amount:
#        print(x)
        # Create variable that will reference the stack that stuff will be moved from
        moving = globals()[stackFrom][-1:]
        # Delete from moving stack
        del globals()[stackFrom][-1:]
#        print(moving)
#        print(globals()[stackFrom])
        # Add to new stack
        for m in moving:
            globals()[stackTo].append(m)
#        print(globals()[stackTo])
        x += 1


# In[ ]:


print(stack1)
print(stack2)
print(stack3)
print(stack4)
print(stack5)
print(stack6)
print(stack7)
print(stack8)
print(stack9)


# In[ ]:


# Part 2


# In[ ]:


with open('data/dec5Input.txt') as d:
    input = d.read().splitlines()
#print(input)
#stack1 = ['Z', 'N']
#stack2 = ['M', 'C', 'D']
#stack3 = ['P']
stack1 = ['G', 'D', 'V', 'Z', 'J', 'S', 'B'] 
stack2 = ['Z', 'S', 'M', 'G', 'V', 'P']
stack3 = ['C', 'L', 'B', 'S', 'W', 'T', 'Q', 'F']
stack4 = ['H', 'J', 'G', 'W', 'M', 'R', 'V', 'Q']
stack5 = ['C', 'L', 'S', 'N', 'F', 'M', 'D']
stack6 = ['R', 'G', 'C', 'D']
stack7 = ['H', 'G', 'T', 'R', 'J', 'D', 'S', 'Q']
stack8 = ['P', 'F', 'V']
stack9 = ['D', 'R', 'S', 'T', 'J']


# In[ ]:


for i in input:
    move = i.split(' ')
    amount = int(move[1])
    original = int(move[3])
    new = int(move[5])
#    print(f'{amount} {original} {new}')
    stackFrom = 'stack' + str(original)
    stackTo = 'stack' + str(new)
#    print(globals()[stackFrom])
    x = 0
    moving = []
    while x < amount:
#        print(x)
        # Create variable that will reference the stack that stuff will be moved from
        moving = globals()[stackFrom][-amount:]
        # Delete from moving stack
        del globals()[stackFrom][-amount:]
#        print(globals()[stackFrom])
        # Add to new stack
#        print(moving)
        for m in moving:
            globals()[stackTo].append(m)
#        print(globals()[stackTo])
        x = amount
#   print(moving)


# In[ ]:


print(stack1)
print(stack2)
print(stack3)
print(stack4)
print(stack5)
print(stack6)
print(stack7)
print(stack8)
print(stack9)


# In[ ]:




