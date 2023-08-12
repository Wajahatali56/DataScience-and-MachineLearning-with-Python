
# Creating a parent class 
class person:
    def __init__(self , fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printinfo(self):
        print(self.firstname , self.lastname)
x = person("wajahat" , "ALI")
x.printinfo()

# Creating a child class

class student(person):
    pass

# Testing the student class
class person:
    def __init__(self , fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printinfo(self):
        print(self.firstname , self.lastname)
class student(person):
    pass
x = student("Muhammad" ,"Arshad")
x.printinfo()

# In that above case , child class will inherit all of its properties and method from our base or parent class

# Adding  __init__() function
class person:
    def __init__(self , fname , lname):
        self.firstname = fname
        self.lastname = lname
    def myfun(self):
        print(self.firstname , self.lastname)
class student(person):
    def __init__(self, fname, lname):
        person.__init__(self ,fname, lname)
x = student("Waji" ,"Developer")
x.myfun()

# using super() function
class person:
    def __init__(self , fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printinfo(self):
        print(self.firstname , self.lastname)
class student(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
x = student("Waji" ,"DeveloperZone")
x.printinfo()

# How to add property
class person:
    def __init__(self , fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printinfo(self):
        print(self.firstname , self.lastname)
class student(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduateyear = 2023
x = student("ALIAN" ,"Python")
print(x.graduateyear)

# you can pass the object property in student directly

class person:
    def __init__(self , fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printinfo(self):
        print(self.firstname , self.lastname)
class student(person):
    def __init__(self, fname, lname ,year):
        super().__init__(fname, lname)
        self.graduateyear = year
x = student("WAJAHAT" , "ALI" , "2028")
print(x.graduateyear)



#__________________BEST OF LUCK ____________________#