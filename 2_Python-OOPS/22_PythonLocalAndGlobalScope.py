
# What is Scope: A variable is only available from inside the region it is created and this is called scope

# Local scope:

def myfunc():
    var = 400
    print(var)
myfunc()

# Function inside the function

def myfunc():
    var = 500
    def myinnerfunc():
        print(var)
    myinnerfunc()
myfunc()

# Global scope:
var = 600

def myfunc():  
    print(var) 
myfunc()

# Naming variables - python will treat 2 or more than 2 variables as a separate variables

var = 700

def myfunc(): 
    var = 100 
    print(var) 
myfunc()
print(var)

# Global keywords - if you need to create a global variables locally then you should use globla keywords

def myfunc(): 
    global var 
    var = 800 
myfunc()
print(var)

# You can also use the global keywords if you wants to make a change to a global variables inside the function

var = 900
def myfunc(): 
    global var 
    var = 1000
myfunc()

print(var)


#__________________BEST OF LUCK ____________________#