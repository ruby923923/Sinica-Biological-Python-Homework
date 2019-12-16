#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
database = {}
max_items = 0

def set_max(x): # set a limit on database size
    global max_items
    max_items = x
    return max_items

# when the number of item reaches maximum
# or the name is already in the database
# , ignore the input and return -1
# otherwise, add the name,grade and return 0
    
def add(name, grade):
    if  len(database)+1 > max_items: 
        return -1
    elif name in database: 
        return -1 
    else:
        database[name] = grade 
        return 0 
    
def remove(name): # remove a name from the database
    database.pop(name)
    
# Print the database in a sorted order
# format: 'Tom:100
#          Jerry:*50
  
def output(): 
    if database == {}: # print '(No data)' when the database is empty 
        print('No data')
    else:
        database_sorted = dict(sorted(database.items(), key=lambda item:item[1], reverse = True))
        for name in database_sorted:
            print(name + ':' + str(database[name]))  

def watchlist(): # return a list of names with grades under 70
    name_list = []
    for name in database:
        if database[name] < 70:
            name_list.append(name)
    return name_list            

def mean_and_max(): # return mean and sum of the database
    database_grade = database.values()
    database_grade_list=list(database_grade)
    Mean = np.mean(database_grade_list)
    Max = np.max(database_grade_list)
    return int(Mean), Max

def find(name): # Return the grade of the name
    if name in database: 
        grade = database[name]
        return grade
    else: # If not found, return -1
        return -1


# In[ ]:




