#!/usr/bin/env python
# coding: utf-8

# In[ ]:


string1 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
string2 = 'nppdvjthqldpwncqszvftbrmjlhg'
string3 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
string4 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
with open('data/dec6Input.txt') as d:
    input = d.read()
print(input)


# In[ ]:


def evaluateList(list):
    if list[0] in list[1:4]:
        return True
    if list[1] in list[2:4]:
        return True
    if list[2] == list[3]:
        return True
    else:
        return False

def string4search(input):
    list = []
    count = -1
    for i in input:
        count += 1
#        print(list)
        if len(list) < 4:
            list.append(i)
#            print(list)
        elif len(list) > 3:
#            print(list)
            match = evaluateList(list)
#            print(match)
            if match == False:
                print(count)
                print(list)
                break
            list.pop(0)
            list.append(i)


    


# In[ ]:


string4search(input)


# In[ ]:


def evaluate14List(list):
    if list[0] in list[1:15]:
        return True
    if list[1] in list[2:15]:
        return True
    if list[2] in list[3:15]:
        return True
    if list[3] in list[4:15]:
        return True
    if list[4] in list[5:15]:
        return True
    if list[5] in list[6:15]:
        return True
    if list[6] in list[7:15]:
        return True
    if list[7] in list[8:15]:
        return True
    if list[8] in list[9:15]:
        return True
    if list[9] in list[10:15]:
        return True
    if list[10] in list[11:15]:
        return True
    if list[11] in list[12:15]:
        return True
    if list[12] == list[13]:
        return True
    else:
        return False

def string14search(input):
    list = []
    count = -1
    for i in input:
        count += 1
#        print(list)
        if len(list) < 14:
            list.append(i)
#            print(list)
        elif len(list) > 13:
#            print(list)
            match = evaluate14List(list)
#            print(match)
            if match == False:
                print(count)
                print(list)
                break
            list.pop(0)
            list.append(i)


# In[ ]:


string14search(input)


# In[ ]:




