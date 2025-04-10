In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType


#ex1
x = 5
print(type(x))

"""
x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType
"""

"""
x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = complex(1j)	complex	
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview

"""

---Python Numbers---
#ex1
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#ex2
print(type(x))
print(type(y))
print(type(z))

#ex3
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#ex4
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#ex5
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#ex6
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#ex7
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#ex8
import random

print(random.randrange(1, 10))

#ex9
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#ex10
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2


#ex11
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

