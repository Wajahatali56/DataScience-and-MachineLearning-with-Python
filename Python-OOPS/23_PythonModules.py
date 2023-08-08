
# What is module:
# Consider a module to be as same as a code library like a file containing a set of functions you want to include in an application.

# Create a module.

import mymodule
mymodule.greeting("Wajahat")

# Variables in modules - A module can contain function but also variables of all types

import mymodule1
x = mymodule1.person1["Age"]
print(x)

# Naming and re-naming a module with as keyword
import mymodule1 as md 
a = md.person1["Subject"]
print(a)

import platform
x = platform.system()
print(x)

# Using the dir() function

import platform
x = dir(platform)
print(x)

# Import from module - using from keyword

from mymodule2 import person1
print(person1["Age"])


#__________________BEST OF LUCK ____________________#
