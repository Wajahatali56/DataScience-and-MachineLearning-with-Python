# try - block let you test a block of code for error.
# except -block let you handle the error.
# else - block lets you the execute the code when there is no error.
# finally -block let you execute code regardless of the try and except block.

# Example of try block 
'''
try:
    print(x)
except:
    print("Error occur") # profession error

# if try and except is not given
# print(X) // unprofessional error

# Using many exceptions

try:
    print(x)
except NameError:
    print("variable of x is not defined")
except:
    print("something else went wrong")
'''
# else - you can use else keyword to define a block of code.

try:
    print("Hello")
except :
    print("something  went wrong")
else:
    print("Nothing went wrong")

# Using Finally block 
'''
try:
    print(X)
except :
    print("something else went wrong")
finally:
    print("the 'try' except is finished")
'''
# Real Example

try:
    f = open("demofile.txt")
    try:
        f.write("hello community")
    except:
        print("something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("something went wrong when opening to the file")

# Raise an exception
'''
x = -1 
if x < 0:
    raise Exception("Sorry , no number is below zero")
    '''

# raise a typeerror if x is not a n integer
str = "ali"
if not type(str) is int:
    raise TypeError("Only integers are allowed")