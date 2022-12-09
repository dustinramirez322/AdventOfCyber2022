#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import string
with open('data/dec3Input.txt') as d:
    input = d.read().splitlines()
#print(input)


# In[ ]:


lowerScore = dict(zip(string.ascii_lowercase, range(1,27)))
upperScore = dict(zip(string.ascii_uppercase, range(27,53)))
#print(lowerScore)
#print(upperScore)
lowerScore.update(upperScore)
#print(lowerScore)


# In[ ]:


totalScore = 0
for i in input:
    length = len(i)
    half = int(length/2)
    firstHalf = i[0:half]
    secondHalf = i[half:]
#    print (firstHalf + ' ' + secondHalf)
    for f in firstHalf:
        if f in secondHalf:
            score = lowerScore[f]
            totalScore += score
            break
        else:
            pass
print(totalScore)


# In[ ]:


q2score = 0
x = 0
newList = []
for i in input:
    if x == 3:
        x = 0
        newList = []
    if x < 3:
        newList.append(i)
        x += 1
        if x == 3:
            for n in newList[0]:
                if n in newList[1]:
                    if n in newList[2]:
                        score = lowerScore[n]
                        q2score += score
                        break
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass
print(q2score)


# In[ ]:




