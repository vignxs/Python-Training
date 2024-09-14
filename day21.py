#!/usr/bin/env python
# coding: utf-8

# 1. What is a Decorator?
# 
# A decorator in Python is a function that modifies
#  the behavior of another function or method. 
# It allows you to add functionality to an existing
#  function without modifying its source code.

# 2. Creating a Simple Decorator:
# 
# Let's start by defining a basic decorator:

# In[2]:


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


# In this example:
# 
# my_decorator is the decorator function.
# wrapper is the inner function that adds functionality.
# func is the function being decorated.
# 
# 
# 3. Decorating a Function:
# 
# Now, let's apply our decorator to a function:

# In[3]:


@my_decorator
def say_hello():
    print("Hello!")


# This syntax @my_decorator is equivalent to say_hello = my_decorator(say_hello).
# 
# 4. Calling the Decorated Function:
# 
# When we call the say_hello() function, it will execute with the added functionality from the decorator:

# In[4]:


say_hello()


# 5. Decorating Functions with Arguments:
# 
# To decorate functions with arguments, we need to use *args and **kwargs in the wrapper function:

# In[4]:


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper


# 6. Preserving Function Metadata:
# 
# To preserve the metadata (such as docstring and name) of the original function, you can use the functools.wraps decorator from the functools module:

# In[8]:


from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper


# 7. Decorator with Arguments (Optional):
# 
# You can create decorators that accept arguments by adding an additional layer of functions:

# In[6]:


def repeat(num_times):
    def decorator_repeat(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


# In[10]:


@repeat(num_times=5)
def greet(name):
    print(f"Hello {name}")


greet("Alice")


# In[11]:


class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Something is happening before the function is called.")
        result = self.func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result


@MyDecorator
def greet(name):
    print(f"Hello, {name}")


greet("Alice")


# Decorator Factory:
# 
# A decorator factory is a function that returns a decorator. This allows you to parameterize your decorators. Here's an example:

# In[9]:


def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}")


greet("Alice")


# yield is a keyword in Python used in generator functions and generator expressions. It allows you to create iterators without the need to build and maintain an entire list in memory at once. Here's how it works:
# 
# 1. Generator Functions:
# 
# Generator functions are functions that contain one or more yield statements. When called, they return a generator object, which can be iterated over to produce values lazily.

# In[13]:


def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()
print(gen)
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3


# In this example, my_generator() is a generator function that yields values 1, 2, and 3 when iterated over.
# 
# 2. Generator Expressions:
# 
# Generator expressions are similar to list comprehensions, but they return a generator object instead of a list. They are created using parentheses () instead of square brackets [].

# In[12]:


gen_exp = (x for x in range(3))

print(type(gen_exp))
print(next(gen_exp))  # Output: 0
print(next(gen_exp))  # Output: 1
print(next(gen_exp))  # Output: 2


# Here, (x for x in range(3)) is a generator expression that yields values from 0 to 2 when iterated over.
# 
# 3. Lazy Evaluation:
# 
# One of the key benefits of using yield is lazy evaluation. Values are generated one at a time, only when needed, which can save memory and improve performance when dealing with large datasets or infinite sequences.
# 
# 

# In[15]:


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


gen = infinite_sequence()
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 2
# Continues infinitely...


# In this example, infinite_sequence() generates an infinite sequence of numbers starting from 0.
# 
# 4. Stateful Generators:
# 
# Generator functions can maintain state between iterations, allowing you to implement complex logic in a concise manner.

# In[20]:


def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value


gen = accumulator()
print(next(gen))     # Output: 0
print(gen.send(0))   # Output: 1
print(gen.send(2))   # Output: 3
print(gen.send(3))   # Output: 6
gen.close()


# When a function encounters a return statement, it immediately exits and returns the specified value to the caller, and the function's state is lost.
# 
# On the other hand, when a function encounters a yield statement, it temporarily suspends its execution and returns the yielded value to the caller. The function's state is preserved, allowing it to resume execution from the same point when called again.
# 
# 

# In[18]:


def generate_numbers_with_return():
    result = []
    for i in range(5):
        result.append(i)
    return result


def generate_numbers_with_yield():
    for i in range(5):
        yield i


# Using return
numbers_return = generate_numbers_with_return()
print(numbers_return)         # Output: [0, 1, 2, 3, 4]

# Using yield
numbers_yield = generate_numbers_with_yield()
# Output: <generator object generate_numbers_with_yield at 0x0000025AC22B8400>
print(numbers_yield)

# Iterating over the generator
for num in numbers_yield:
    print(num)                # Output: 0, 1, 2, 3, 4


# In this example:
# 
# generate_numbers_with_return() returns a list containing numbers from 0 to 4.
# generate_numbers_with_yield() is a generator function that yields numbers from 0 to 4 one at a time.
# Iterating over the generator produced by generate_numbers_with_yield() yields the numbers one by one without storing them all in memory at once.

# In[ ]:




