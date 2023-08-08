
# Sort the list alphabetically
x = ["banana" , "orange" , "apple" , "mangoes" , "gava" ]
x.sort()
print(x)

# Sort the list Numerically
x = [10 , 20 , 50 , 56, 12 , 2 , 45, 67]
x.sort()
print(x)

# Sorting lists in descending order

x = ["banana" , "orange" , "apple" , "mangoes" , "gava" ]
x.sort(reverse=True)
print(x)

# Sorting lists of numeric values in descending order

x = [10 , 20 , 50 , 56, 12 , 2 , 45, 67]
x.sort(reverse=True)
print(x)

# Customize sort functions 
# Hint : we are trying to print nearby '50' elements 
# And tell me about abs() function
def myfunc(n):
    return abs(n-50)   # abs is math function abs(n) = 100 by default
x = [10 , 20 , 50 , 56, 12 , 2 , 45, 67]
x.sort(key=myfunc)
print(x)
# OUTPUT : [50, 45, 56, 67, 20, 12, 10, 2]
# Reverse the sorting order
x = ["banana" , "orange" , "apple" , "mangoes" , "gava" ]
x.reverse()
print(x)

# Copy a list

x = ["banana" , "orange" , "apple" , "mangoes" , "gava" ]
newlist = x.copy()
print(newlist)

# Make a copy of list with build-in method 
x = ["banana" , "orange" , "apple" , "mangoes"]
y = list(x)
print(y)

# Joining the lists 
x = ["banana" , "orange" , "apple" , "mangoes"]
y = [10 , 20 , 50 , 56, 12 , 2 , 45, 67]
z = x + y
print(z)

# Another way of joining through append()

x = ["banana" , "orange" , "apple" , "mangoes"]
y = [10 , 20 , 50 , 56, 12 , 2 , 45, 67]
for i in y:
    x.append(i)
print(x)

# Another way of joining through Extend()
x = ["banana" , "orange" , "apple" , "mangoes"]
y = [10 , 20 , 50 , 56, 12 , 2 , 45, 67]
x.extend(y)
print(x)


'''
# List methods
append()
clear() 
extend()
copy()
index()
remove()
reverse()
sort()
pop()
count()
insert() '''



#__________________BEST OF LUCK ____________________#