
# Python conditions and if statements:

# Equal       x == y
# Not equal   x != y
# less than    x < y
# less than or equal to   x <= y
# greater than   x > y
# greater than or equal to  x >= y

# Example of if statement

x = 20
y = 100
if x < y:
    print("Yes , 'x' is less than 'y':")

# Elif keyword is used when previous condition is not true 

x = 100
y = 100
if x > y:
    print("x is greater than y")
elif x==y:
    print("x and y are same") 

# Else catches anything which isn't cought by any preceeding conditions

x = 20
y = 100
if x > y: 
    print("x is greater than y")
elif x == y:
    print("x and y are equal")
else:
    print("y is greater than x") 

# You can also have an else without elif
x = 20
y = 100
if x > y: 
    print("x is greater than y")
else:
    print("y is greater than x")

# Short hand  if
x = 20
y = 100
if x < y: print("x is less than y")

# Short hand if .... else 

x = 200
y = 100
print("x is greater than y") if x > y else print("x is lesser than y")

# one line if else statement with 3 conditions 
x = 200
y = 200
print("A") if x > y else print("x and y are equal") if x == y else print("B")

# And is a logical operator and it is used to combine the conditional statements
x = 200
y = 400
z = 600
if x < y and z > y:
    print("Both the conditions are true:")


# or is a logical operator and it is used to combine the logical statements
x = 200
y = 400
z = 600
if x < y or z < y:
    print("Only one conditions is true:")

# Nested if statement: you can have if statement inside of statement.

x = 40
if x > 10:
    print("It is above 10, ")
    if x > 20:
          print("It is also above 20")
    else:
        print("It is not above 20")

# The pass statement - if in case of reason if statement has no content than you can pass the statement for avoiding the error in program 

x = 200
y = 400
if x < y:
    pass



#__________________BEST OF LUCK ____________________#




