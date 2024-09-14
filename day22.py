#!/usr/bin/env python
# coding: utf-8

# ### Lambda functions, also known as anonymous functions, are small, inline functions that can have any number of arguments but can only have one expression. They are defined using the lambda keyword. Lambda functions are handy when you need a simple function for a short period and don't want to define a separate function using the def keyword.

# lambda arguments: expression
# 
# Let's break it down:
# 
# lambda: The keyword used to declare a lambda function.
# arguments: Comma-separated list of input parameters (arguments) to the function.
# expression: The computation to be performed with the arguments. The result of this expression is returned when the lambda function is called.

# In[1]:


def add(x, y): 
    return x + y


print(add(3, 5))  # Output: 8


# In[2]:


add = lambda x, y: x + y
print(add(3, 5))  # Output: 8


# In[3]:


square = lambda x: x ** 2
print(square(8))  # Output: 16


# lambda pair: pair[1] defines a lambda function that takes a tuple pair and returns its second element. This lambda function is used as the key function for sorting the list of tuples based on their second element
# s.

# In[4]:


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)  # Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]


# In[5]:


x = [ i for i in range(10)]
x


# Dictionary comprehensions provide a concise way to create dictionaries in Python. They allow you to transform or filter elements from an iterable (e.g., lists, tuples, or strings) and construct dictionaries using a compact and readable syntax.
# 
# Here's the basic syntax of a dictionary comprehension:
# 
# python
# Copy code
# ## {key_expression: value_expression for item in iterable if condition}
# Let's break it down:
# 
# {key_expression: value_expression}: The key-value pair to include in the resulting dictionary.
# for item in iterable: The iteration over each item in the iterable.
# if condition (optional): An optional condition that filters the items included in the resulting dictionary.

# In[8]:


squares_dict = {x: x ** 2 for x in range(5)}
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# In[9]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_dict = {x: x ** 2 for x in numbers if x % 2 == 0}
print(even_numbers_dict)  # Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}


# In[10]:


keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined_dict = {k: v for k, v in zip(keys, values)}
print(combined_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}


# In[6]:


word = "helloo"
char_freq = {char: word.count(char) for char in word}
print(char_freq)  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}


# The map() function in Python applies a given function to each item of an iterable (such as a list, tuple, or string) and returns a map object (an iterator) that yields the results.
# 
# Here's the basic syntax of the map() function:
# 
# python
# ## map(function, iterable)
# function: The function to apply to each item of the iterable.
# iterable: The iterable (e.g., list, tuple, string) whose elements will be passed to the function.
# The map() function can accept multiple iterables, and the function should accept the same number of arguments as the number of iterables provided. It will then iterate over each element of the iterables in parallel.

# In[9]:


numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)
print(list(doubled))  # Output: [2, 4, 6, 8, 10]


# In[10]:


strings = ["apple", "banana", "cherry"]
uppercase_strings = map(str.upper, strings)
print(list(uppercase_strings))  # Output: ['APPLE', 'BANANA', 'CHERRY']


# In[11]:


list1 = [1, 2, 3]
list2 = [4, 5, 6]
sums = map(lambda x, y: x + y, list1, list2)
print(list(sums))  # Output: [5, 7, 9]


# In[15]:


def sum_of_numbers(n):
    # Base case: If n is 0, return 0
    if n == 0:
        return 0
    # Recursive case: Add n to sum of (n-1)
    else:
        return n + sum_of_numbers(n - 1)


# Test the function
print(sum_of_numbers(2))  # Output: 15 (1 + 2 + 3 + 4 + 5)


# In[16]:


def fibonacci(n):
    # Base case: If n is 0 or 1, return n
    if n == 0 or n == 1:
        return n
    # Recursive case: Fibonacci of n is sum of Fibonacci of (n-1) and (n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Test the function
print(fibonacci(6))  # Output: 8 (0, 1, 1, 2, 3, 5, 8)

