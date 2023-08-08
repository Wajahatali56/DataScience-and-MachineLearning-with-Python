

# Syntex :
#             lambda argument : expression


x = lambda a : a * 10
print(x(2))

# Lambda function can even take multiple arguments and return results

x = lambda a , b: a * b
print(x(2 , 4))

# 3 arguments in lambda function
x = lambda a , b , c: a * b + c
print(x(2 , 4 ,2))

# Why we use lambda function
def my_fun(n):
    return lambda a: a * n 
my_double = my_fun(2)
print(my_double(11))

# New function for double and triple 

def my_fun(n):
    return lambda a: a * n  # for unknown function 
my_double = my_fun(2)
my_triple = my_fun(3)
print(my_double(11))
print(my_triple(11))

#__________________BEST OF LUCK ____________________#
