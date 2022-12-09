#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = 'rock'
b = 'paper'
c = 'scissors'
x = 'rock'
y = 'paper'
z = 'scissors'
xNum = 1
yNum = 2
zNum = 3

lose = 0
draw = 3
win = 6
total = 0


# In[ ]:


with open('data/rpsStrat.txt') as r:
    strat = r.read().splitlines()
print(strat)


# In[ ]:


scores = {'A X': 4, 'A Y': 8, 'A Z': 3, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 7, 'C Y': 2, 'C Z': 6}


# In[ ]:


# X = lose
# Y = draw
# Z = win
# rock = 1
# paper = 2
# scissors = 3
newScores = {'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}


# In[ ]:


# used for scores
total = 0
for s in strat:
    for k, v in scores.items():
        if s == k:
            outcome = v
        else:
            pass
    total += outcome


# In[ ]:


# used for new scores
total = 0
for s in strat:
    for k, v in newScores.items():
        if s == k:
            outcome = v
        else:
            pass
    total += outcome        


# In[ ]:


print(total)


# In[ ]:




