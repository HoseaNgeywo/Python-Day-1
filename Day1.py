# Introduction to python
# Comments
print('hi')
# if 5 > 22:
#    print("Five is greater than two")
x = 10
y = 0.3
z = "Hosea"

# Get the type of a variable
print(type(y))


# Variables
# variables are case sensitive
# Cannot start with numbers

# unpacking from list

fruits = ['apple', 'banana', 'cherry', 'maize']
x, y, z, m = fruits
print(x)


# Global variables
x = 'awesome'

def myfun():
    x = 'great'
    print("Programming is " + x)
    
myfun()

# Global keyword
def myglobal():
    global y 
    y = 'fantastic'
myglobal()
print(y)

# complex = 1j
# set ={}
# frozenset = ({})
# bytes = b'hello'
# bytearray(5)
# memoryview(bytes(5))

# Numbers
m = 5e3
# print(type(m))
print(m)

import random
t = random.randrange(1, 15)
print(t)

# Casting converting a variable from one type to another


# Strings are array
# Loop the strings through for loop

for x in 'banana':
    print(x)

# len() - Get the length
# in - check if a given phrase is present in a string
# not in

# Slicing characters in a string

g = 'congratulations'
print(g[1:])
print(g[2:5])
print(g[:7])
print(g[-2:])

# Modify strings
a = 'lower primary school'
b = '   UPPER PRIMARY SCHOOL'
print(a.upper())
print(b.lower())

# strip() - Remove whitespace
print(b.strip())

# Replace() String with another

print(a.replace('l', 'm'))

# split() string to list
print(a.split(','))
c = a.split(',')
print(type(c))

