
# Arithmatic Operators
# Assignment Operators
# Comparison Operators
# Logical Operators
# Identity Operators
# membership operators
# Bitwise Operators

# Arithmatic Operators:
x = 10
y = 2
print(x+y)

x = 10
y = 2
print(x-y)

x = 10
y = 2
print(x/y)

x = 10
y = 2
print(x%y) #Modulus for remainder

x = 10
y = 2
print(x**y) # exponential operator , it takes power

# Assignment Operators:

# x = 5
# x = x + 5 same as x += 5
# x = x - 5 same as x -= 5
# x = x * 5 same as x *= 5
# x = x / 5 same as x /= 5
# x = x % 5 same as x %= 5
# x = x ** 5 same as x **= 5

x = 5 
x *= 3
print(x)

# Comparison Operators:

x = 5
y = 3
print(x == y) # Equal to

x = 5
y = 3
print(x != y) # Not equal to

x = 5
y = 3
print(x > y) # Greater than operator

x = 5
y = 3
print(x < y) # lesser than operator

x = 5
y = 3
print(x >= y) # Greater than and equal to operator

x = 5
y = 3
print(x <= y) # lesser than and equal to operator

# Logical Operators:

 # Types  : AND   OR     NOT 

# AND 
x = 5 
print(x>3 and x<10)

# OR
x = 5 
print(x>3 or x<2)

# NOT  : reverse the result
x = 5 
print(not(x>3 or x<2))

# Identity Operators: Is used to compare any kind of object; And not used when object are same and same memory location

# Is 
# Is not 

x = ["Wajahat" , "Ali"]
y = ["Wajahat" , "Ali"]
z = x
print(x is z) # it will return true because z is the same object as x.


print(x is y) # Return false because x is not the same object as y even if they have the same content.

print(x == y) # To demonstrate the difference between "is" and "==" , this comparison will return True because x is equal to y.

# membership operators:
# It is used to test the sequences (find and replace) 
# in 
# not in

x = ["apple" , "Banana" , "orange" , "gava"]
print("Banana" in x)

x = ["apple" , "Banana" , "orange" , "gava"]
print("Adding" not in x)

#__________________BEST OF LUCK ____________________#