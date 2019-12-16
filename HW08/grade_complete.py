#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
import csv
database = {}
max_items = 0

# save the database to a file 
# remember max_items!
def save(filename):
    with open(filename,'w') as file:
        file.write(str(database))
        
# reload the database from a file
def load(filename): 
    try:
        with open(filename,'r') as file:
            file.read()
    except IOError:
        print('File not found')
        
# save to CSV format 
# no need to export max_items here
def export_to_txt(filename): 
    name = list(database)
    score = list(database.values())
    k = []
    for i in zip(name,score):k.extend(list(i))
    x = [k[i:i+2] for i in range(0, len(k),2)]
    with open(filename,'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in x:
            writer.writerow(i)
    
# import from CSV format
# set_max is set as the number of items
# in the loaded file
def import_from_txt(filename):
    global database
    database = {}
    try:
        with open(filename,newline = '') as csvfile:
            filereader = csv.reader(csvfile)
            for row in filereader:
                key = row[0]
                database[key] = int(row[1])
    except:
        print('File not found')
                       

##########################################            
def set_max(x): # set a limit on database size
    global max_items
    if int(x) != x:
        raise ValueError('Test')
    else:
        max_items = x
    return max_items

# when the number of item reaches maximum
# or the name is already in the database
# , ignore the input and return -1
# otherwise, add the name,grade and return 0
    
def add(name, grade):
    if grade < 0 or grade > 100:
        raise ValueError    
    elif  len(database)+1 > max_items: 
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
            if database[name] < 70:
                print('*'+ name + ':' + str(database[name])) 
            else:
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

