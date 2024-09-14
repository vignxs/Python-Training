#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#File handling


# In[5]:


with open('notes.txt') as file_object:    
    contents = file_object.read()
    print(type(contents))
    


# In[ ]:


print(contents.rstrip())


# In[10]:


filename = 'notes.txt'

with open(filename) as file_object:    
    for line in file_object:    
        # print(line)
        print(line.rstrip())


# In[58]:


filename = 'notes.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

# for line in lines:
    # print(line)
    # print(line.rstrip())
    
lines


# In[19]:


filename = 'programming.txt' 

with open(filename, 'w') as file_object:  
    file_object.write("I love programming. \n")
    file_object.write("vignesh")
    print("file created successfully")


# In[27]:


filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I love programming. \n")
    file_object.write("vignesh\n")
    print("file created successfully")


# In[52]:


filename = 'programming1.txt'
file_object = open(filename, 'w')

file_object.write("I love programming. \n")

file_object.close()


# In[60]:


import os

os.remove("programming.txt")


# In[63]:


import os
if os.path.exists("programming1.txt"):
  os.remove("programming1.txt")
else:
  print("The file does not exist")

