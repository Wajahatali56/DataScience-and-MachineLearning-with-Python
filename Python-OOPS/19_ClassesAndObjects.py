
# Python is an object-oriented language

# Create a class
class myclass:
    x = 55
    y = 10.9
    z = x + y
print(myclass)

# Create object
class my_class:
    x = 5
    y = 10.9
    z = x + y
m1 = my_class() # m1 is object
print(m1.z)
print(m1.x)

# The_init_() function : built-in for classes

class person:
    def __init__(self , name , age):
        self.name = name 
        self.age = age 
p1 = person("Wajahat" , 20)
print(p1.name)
print(p1.age)

# Object method
class person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def my_fun(self):
        print("Hello everyone , my name is " + self.name)
p1 = person("ALi" , 45)
p1.my_fun()

# Self parameter
class person:
    def __init__(xyz , name , age):
        xyz.name = name
        xyz.age = age
    def myfun(abc):
        print("Hello everyone , my name is " + abc.name)
p1 = person("nawaz" , 34)
p1.myfun()

# How to modify object property
class person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def myinfo(self):
        print("Hello everyone , my name is " + self.name)
p1 = person("Haider" , 36)
p1.age = 40
print(p1.age)

# Delete  object properties
class info:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def myinfo(self):
        print("Hello everyone , my name is " + self.name)
p1 = person("Haider" , 36)
# keyword : del
del p1.age
print(p1.name)

# How to delete object
class person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def myinfo(self):
        print("Hello everyone , my name is " + self.name)
p1 = person("Haider" , 36)
del p1

# The pass statement

class person:
    pass



#__________________BEST OF LUCK ____________________#






