#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

database = {}

print("input name and grade. Terminated when name is'OK'")

while 1:
    name = input('Enter name:')
    if name == 'OK':
        break
    elif name in database:
        print('Already in database')
    else:
        grade = float(input('Grade:'))
        database[name]=grade

print()


# In[24]:


print('Grade database')
database_name = database.keys()
database_grade = database.values()
database_sort = sorted(database_name, key=database.get, reverse=True)

for k in database_sort:
    if database[k] < 60:
        print('*'+ k + ':' + str(database[k]))
    else:
        print(k + ':' + str(database[k]))

database_grade_list=list(database_grade)
Mean = np.mean(database_grade_list)
Max = np.max(database_grade_list)
print('Mean: %f' % Mean + ', ' + 'Max: %f' % Max)


# In[10]:


name_to_find = input('Name to find: ')

if name_to_find in database:
    the_grade = database[name_to_find]
    if the_grade < 60:
        print('! %f' %the_grade)
    else:
        print('%f' %the_grade)
else:
    print('Not found')
    
    


# In[21]:


grade_to_find = float(input('Grade to find: '))

if grade_to_find not in database.values():
    print('Not found')
else:
    for the_name in database:
        if database[the_name] == grade_to_find:
            print('%s' %the_name)
        


# In[ ]:




