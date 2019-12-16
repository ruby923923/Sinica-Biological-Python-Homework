#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np

database = []

print("input name and grade. Terminated when name is'OK'")

while 1:
    name = input('Enter name:')
    if name == 'OK':
        break
    elif name in database:
        print('Already in database')
    else:
        grade = float(input('Grade:'))
        database.append(name)
        database.append(grade)
   


# In[45]:


database_decorated = {}
i = 0
for i in range(0, len(database), 2):
    database_decorated[database[i]] = database[i+1]

print('Grade database')
database_sorted = dict(sorted(database_decorated.items(), key=lambda item:item[1], reverse = True))

for i,j in database_sorted.items():
    if j < 60:
        print('*',i,':',j)
    else:
        print(i,':',j)
        
database_grade_list=list(database_sorted.values()) 
Mean = np.mean(database_grade_list)
Max = np.max(database_grade_list)
print('Mean: %f' % Mean + ', ' + 'Max: %f' % Max)


# In[46]:


name_to_find = input('Name to find: ')

if name_to_find in database:
    the_grade = database_sorted[name_to_find]
    if the_grade < 60:
        print('! %f' %the_grade)
    else:
        print('%f' %the_grade)
else:
    print('Not found')


# In[42]:


grade_to_find = float(input('Grade to find: '))

if grade_to_find not in database_sorted.values():
    print('Not found')
else:
    for the_name in database_sorted:
        if database_sorted[the_name] == grade_to_find:
            print('%s' %the_name)


# In[ ]:




