#!/usr/bin/env python
# coding: utf-8

# # Try Except

# In[18]:


num = 0


print("entered number: ", num)

try:

    print(5/int(num))

    
except ZeroDivisionError:
    print("Error ZeroDivisionError you can not enter 0 to divide another number")


# In[20]:


num = 0


print("entered number: ", num)

try:

    print(5/int(num))


except ZeroDivisionError:
    print("Error ZeroDivisionError you can not enter 0 to divide another number")
    
else:
    print("else block is runnning")


# In[22]:


num = 9


print("entered number: ", num)

try:

    print(5/int(num))


except ZeroDivisionError:
    print("Error ZeroDivisionError you can not enter 0 to divide another number")

else:
    print("else block is runnning")
    
finally:
    print("code ran successfully")


# In[23]:


filename = 'alice.txt'
with open(filename, encoding='utf-8') as f:    
    contents = f.read()


# In[26]:


filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:    
    print(f"Sorry, the file {filename} does not exist.")


# In[30]:


filename = 'alice.txt'
try:
    contents = f.read()

    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except Exception as e:
    print(str(e))

