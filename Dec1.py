#!/usr/bin/env python
# coding: utf-8

# In[ ]:


with open('data/calories.txt') as c:
    calories = c.read().splitlines()
print(calories)


# In[ ]:


intCal = []
for l in calories:
    if l == '':
        intCal.append(l)
    else:
        l = int(l)
        intCal.append(l)
print(intCal)


# In[ ]:


total = 0
totalList = []
for i in intCal:
    if type(i) == int:
        total = total + i
    else:
        totalList.append(total)
        total = 0


# In[ ]:


sorted(totalList)
print(totalList[-1])
topThree = [totalList[-1], totalList[-2], totalList[-3]]
answer = 0
for x in topThree:
    answer += x
print(answer)


# In[ ]:




