# Python Concepts Reference Guide

A comprehensive reference for core Python concepts with clear examples and explanations.

---

## Table of Contents

1. [Data Types](#data-types)
2. [Conditionals](#conditionals)
3. [Loops](#loops)
4. [Functions](#functions)
5. [Iterables & Iterators](#iterables--iterators)
6. [File Operations](#file-operations)
7. [Object-Oriented Programming](#object-oriented-programming)
8. [Scopes & Closures](#scopes--closures)
9. [Decorators](#decorators)

---

## Data Types

### Strings

Immutable sequences of characters.

```python
# Creating strings
single = 'Hello'
double = "World"
multiline = """This is
a multiline string"""

# String operations
text = "Python"
print(text[0])           # 'P' - indexing
print(text[-1])          # 'n' - negative indexing
print(text[0:3])         # 'Pyt' - slicing
print(text.upper())      # 'PYTHON'
print(text.lower())      # 'python'
print(len(text))         # 6

# String methods
print("hello".capitalize())              # 'Hello'
print("Hello World".split())             # ['Hello', 'World']
print("-".join(['a', 'b', 'c']))        # 'a-b-c'
print("  spaces  ".strip())              # 'spaces'
print("hello".replace('l', 'L'))        # 'heLLo'

# F-strings (Python 3.6+)
name = "Alice"
age = 30
print(f"My name is {name} and I'm {age}")
print(f"Next year: {age + 1}")
```

### Integers

Whole numbers with unlimited precision.

```python
# Basic operations
x = 10
y = 3

print(x + y)    # 13 - addition
print(x - y)    # 7  - subtraction
print(x * y)    # 30 - multiplication
print(x / y)    # 3.333... - division (float)
print(x // y)   # 3  - floor division
print(x % y)    # 1  - modulus (remainder)
print(x ** y)   # 1000 - exponentiation

# Type conversion
print(int("42"))        # String to int
print(int(3.9))         # Float to int (truncates)
```

### Floats

Floating-point numbers (decimals).

```python
# Creating floats
pi = 3.14159
scientific = 1.5e-3  # 0.0015

# Operations
print(5.5 + 2.3)     # 7.8
print(10 / 3)        # 3.333...
print(round(3.14159, 2))  # 3.14

# Type conversion
print(float("3.14"))      # String to float
print(float(5))           # Int to float
```

### Booleans

True or False values.

```python
# Boolean values
is_active = True
is_complete = False

# Boolean operations
print(True and False)    # False
print(True or False)     # True
print(not True)          # False

# Comparison operators
print(5 > 3)             # True
print(5 == 5)            # True
print(5 != 3)            # True

# Truthy and Falsy values
# Falsy: False, None, 0, 0.0, '', [], {}, ()
# Everything else is Truthy
print(bool(0))           # False
print(bool("text"))      # True
print(bool([]))          # False
print(bool([1, 2]))      # True
```

### Collections

```python
# Lists - mutable, ordered
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits[0] = "apricot"

# Tuples - immutable, ordered
coordinates = (10, 20)
x, y = coordinates  # unpacking

# Sets - mutable, unordered, unique
unique_numbers = {1, 2, 3, 3, 2}  # {1, 2, 3}
unique_numbers.add(4)

# Dictionaries - key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "NYC"
}
print(person["name"])
person["email"] = "alice@example.com"
```

---

## Conditionals

Control flow based on conditions.

```python
# Basic if-elif-else
age = 18

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

# Ternary operator (conditional expression)
status = "adult" if age >= 18 else "minor"

# Multiple conditions
score = 85
if score >= 90 and score <= 100:
    print("A grade")
elif 80 <= score < 90:  # Chained comparison
    print("B grade")

# Checking membership
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Found apple")

# Checking None
value = None
if value is None:
    print("Value is None")
```

---

## Loops

Iterating over sequences or repeating actions.

### For Loops

```python
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range()
for i in range(5):          # 0 to 4
    print(i)

for i in range(2, 10, 2):   # Start, stop, step
    print(i)                # 2, 4, 6, 8

# Enumerate - get index and value
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Iterating over dictionaries
person = {"name": "Alice", "age": 30}
for key, value in person.items():
    print(f"{key}: {value}")

# List comprehension (concise loop)
squares = [x**2 for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]
```

### While Loops

```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Break statement - exit loop
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
    print(f"You entered: {user_input}")

# Continue statement - skip to next iteration
for i in range(5):
    if i == 2:
        continue  # Skip 2
    print(i)      # Prints 0, 1, 3, 4

# Else clause - runs if loop completes normally
for i in range(3):
    print(i)
else:
    print("Loop completed")
```

---

## Functions

Reusable blocks of code.

```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Multiple parameters with default values
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25 (uses default)
print(power(5, 3))   # 125

# Multiple return values
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

minimum, maximum, total = get_stats([1, 2, 3, 4, 5])

# Variable arguments (*args)
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4))  # 10

# Keyword arguments (**kwargs)
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")

# Lambda functions (anonymous functions)
square = lambda x: x ** 2
add = lambda x, y: x + y

print(square(5))     # 25
print(add(3, 4))     # 7

# Using lambdas with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Type hints (Python 3.5+)
def add_numbers(a: int, b: int) -> int:
    return a + b
```

---

## Iterables & Iterators

Working with sequences efficiently.

```python
# Iterable - any object that can be looped over
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_string = "abc"

# Iterator - object with __next__() method
my_iter = iter(my_list)
print(next(my_iter))  # 1
print(next(my_iter))  # 2

# Generators - functions that yield values
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)  # 5, 4, 3, 2, 1

# Generator expressions (like list comprehensions)
squares_gen = (x**2 for x in range(5))
print(sum(squares_gen))  # 30

# Built-in iterator functions
numbers = [1, 2, 3, 4, 5]

# map - apply function to each element
doubled = list(map(lambda x: x * 2, numbers))

# filter - keep elements that match condition
evens = list(filter(lambda x: x % 2 == 0, numbers))

# zip - combine iterables
names = ["Alice", "Bob"]
ages = [25, 30]
combined = list(zip(names, ages))  # [('Alice', 25), ('Bob', 30)]

# Custom iterable class
class Counter:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max_num:
            self.current += 1
            return self.current
        raise StopIteration

for num in Counter(3):
    print(num)  # 1, 2, 3
```

---

## File Operations

Reading from and writing to files.

```python
# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("Second line\n")

# Reading entire file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # Remove newline

# Reading into a list
with open('example.txt', 'r') as file:
    lines = file.readlines()  # List of lines

# Appending to a file
with open('example.txt', 'a') as file:
    file.write("Appended line\n")

# File modes
# 'r'  - read (default)
# 'w'  - write (overwrites)
# 'a'  - append
# 'r+' - read and write
# 'b'  - binary mode (e.g., 'rb', 'wb')

# Working with file paths
import os

# Check if file exists
if os.path.exists('example.txt'):
    print("File exists")

# Get file size
size = os.path.getsize('example.txt')

# Working with JSON
import json

# Writing JSON
data = {"name": "Alice", "age": 30}
with open('data.json', 'w') as file:
    json.dump(data, file, indent=2)

# Reading JSON
with open('data.json', 'r') as file:
    loaded_data = json.load(file)

# Working with CSV
import csv

# Writing CSV
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 30])

# Reading CSV
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

---

## Object-Oriented Programming

Organizing code with classes and objects.

```python
# Basic class
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"
    
    # String representation
    def __str__(self):
        return f"{self.name} is {self.age} years old"

# Creating objects
buddy = Dog("Buddy", 3)
miles = Dog("Miles", 5)

print(buddy.bark())      # Buddy says Woof!
print(buddy.species)     # Canis familiaris
print(buddy)             # Buddy is 3 years old

# Inheritance
class GoldenRetriever(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)  # Call parent constructor
        self.color = color
    
    # Method overriding
    def bark(self):
        return f"{self.name} says Woof! Woof!"
    
    # New method
    def fetch(self):
        return f"{self.name} is fetching!"

charlie = GoldenRetriever("Charlie", 2, "golden")
print(charlie.bark())    # Charlie says Woof! Woof!
print(charlie.fetch())   # Charlie is fetching!

# Encapsulation (private attributes)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500

# Property decorator
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @full_name.setter
    def full_name(self, name):
        first, last = name.split()
        self.first_name = first
        self.last_name = last

person = Person("John", "Doe")
print(person.full_name)       # John Doe
person.full_name = "Jane Smith"
print(person.first_name)      # Jane

# Class methods and static methods
class MathOperations:
    @classmethod
    def from_string(cls, calculation):
        # Class method - has access to the class
        return cls()
    
    @staticmethod
    def add(x, y):
        # Static method - no access to class or instance
        return x + y

print(MathOperations.add(5, 3))  # 8

# Abstract base classes
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print(rect.area())       # 15
```

---

## Scopes & Closures

Understanding variable visibility and lifetime.

```python
# LEGB Rule: Local, Enclosing, Global, Built-in

# Global scope
x = "global"

def outer():
    # Enclosing scope
    x = "enclosing"
    
    def inner():
        # Local scope
        x = "local"
        print(x)  # local
    
    inner()
    print(x)  # enclosing

outer()
print(x)  # global

# Global keyword
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # 1

# Nonlocal keyword
def outer():
    x = 10
    
    def inner():
        nonlocal x
        x += 5
        print(x)  # 15
    
    inner()
    print(x)  # 15

outer()

# Closures - inner function remembers enclosing scope
def make_multiplier(n):
    def multiplier(x):
        return x * n  # Remembers 'n' from enclosing scope
    return multiplier

times_3 = make_multiplier(3)
times_5 = make_multiplier(5)

print(times_3(10))  # 30
print(times_5(10))  # 50

# Practical closure example - counter
def make_counter():
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

counter1 = make_counter()
counter2 = make_counter()

print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 1 (separate counter)

# Closure with multiple functions
def make_account(initial_balance):
    balance = initial_balance
    
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance
    
    def withdraw(amount):
        nonlocal balance
        if amount <= balance:
            balance -= amount
            return balance
        return "Insufficient funds"
    
    def get_balance():
        return balance
    
    return deposit, withdraw, get_balance

deposit, withdraw, get_balance = make_account(1000)
print(deposit(500))      # 1500
print(withdraw(200))     # 1300
print(get_balance())     # 1300
```

---

## Decorators

Functions that modify other functions.

```python
# Basic decorator
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function
# Hello!
# After function

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!

# Preserving function metadata
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator executed")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """This is the example function."""
    pass

print(example.__name__)  # example (not 'wrapper')
print(example.__doc__)   # This is the example function.

# Practical decorators

# Timing decorator
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

slow_function()

# Logging decorator
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

add(3, 5)

# Caching decorator
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Much faster with memoization

# Class decorators
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Initializing database")

db1 = Database()  # Initializing database
db2 = Database()  # Uses existing instance
print(db1 is db2)  # True

# Method decorators
class MyClass:
    @staticmethod
    def static_method():
        print("Static method")
    
    @classmethod
    def class_method(cls):
        print(f"Class method of {cls.__name__}")
    
    @property
    def my_property(self):
        return "Property value"

obj = MyClass()
MyClass.static_method()
MyClass.class_method()
print(obj.my_property)
```

---

## Additional Resources

**Official Documentation**: [python.org/doc](https://docs.python.org/)

**PEP 8 Style Guide**: [pep8.org](https://pep8.org/)

**Python Package Index (PyPI)**: [pypi.org](https://pypi.org/)

---

## Quick Reference

**Common Built-in Functions**:
- `print()`, `input()`, `len()`, `type()`, `range()`
- `max()`, `min()`, `sum()`, `abs()`, `round()`
- `sorted()`, `reversed()`, `enumerate()`, `zip()`
- `map()`, `filter()`, `all()`, `any()`

**String Formatting**:
```python
name = "Alice"
age = 30

# F-strings (recommended)
f"Name: {name}, Age: {age}"

# format() method
"Name: {}, Age: {}".format(name, age)

# % operator (old style)
"Name: %s, Age: %d" % (name, age)
```

**Exception Handling**:
```python
try:
    risky_operation()
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("No errors occurred")
finally:
    print("Always executes")
```

---

Made with ❤️ for Python learners
