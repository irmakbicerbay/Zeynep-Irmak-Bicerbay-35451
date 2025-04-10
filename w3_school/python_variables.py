#ex1
x = 5
y = "John"
print(x)
print(y)

#ex2
x = 4
x = "Sally"
print(x)


#ex3
x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

#ex4
x = 5
y = "John"
print(type(x))
print(type(y))

#ex5
x = "John"
print(x)
#double quotes are the same as single quotes:
x = 'John'
print(x)

#ex6
a = 4
A = "Sally"

print(a)
print(A)

#ex7
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#ex8 Camel Case Each word, except the first, starts with a capital letter:
myVariableName = "John"
#ex9 Pascal Case Each word starts with a capital letter:
MyVariableName = "John"
#ex10 Snake Case
my_variable_name = "John"

#ex11
Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

#ex12
One Value to Multiple Variables
x = y = z = "Orange"

print(x)
print(y)
print(z)

#ex13
Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

#ex14
Output Variables
x = "Python is awesome"
print(x)

#ex15
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#ex16
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#ex17
x = 5
y = 10
print(x + y)

#ex18
x = 5
y = "John"
print(x, y)

#ex19
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#ex20
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#ex21
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#ex22
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#
