# Indexing are included : 1st object replaces 0 index
x = ["Banana" , "orange" , "apple"]
print(x)

# Duplicate values

x = ["Banana" , "orange" , "apple" , "apple"]
print(x)

# List length 
x = ["Banana" , "orange" , "apple" , "apple"]
print(len(x))

# List items - Data types
x = ["a" ,"b","c"]
y = [1,4,6,7,9]
z = [True , False , True]
print(x)
print(y)
print(z)
# A List with string ,int and boolean

a = ["wajahat" , 5 , True , 10 ,"ali"]
print(a)

# Data types for lists
a = ["wajahat" , 5 , True , 10 ,"ali"]
print(type(a))

# List[] Constructor

a = list(("wajahat" , 5 , True , 10 ,"ali"))
print(a) # Double round brackets (( )) same as square brackets []

# Python collections (Arrays)

# 4 types of data types in python : 1) Lists  2) Tuples  3) Set  4) Dictionary
# Sets are unchange able -

# How to access items
x = ["Banana" , "orange" , "apple"]
print(x[2])

# Range of indexes
x = ["Banana" , "orange" , "apple" , "mangoes" , "gava" , "sting" , "Coca-cola"]
print(x[2:5])

# Negative indexing 
x = ["Banana" , "orange" , "apple" , "mangoes" , "gava" , "sting" , "Coca-cola"]
print(x[-6:-1])

# Leaving out the start values 

x = ["Banana" , "orange" , "apple" , "mangoes" , "gava" , "sting" , "Coca-cola"]
print(x[:4])

# Leaving out the End values 
x = ["Banana" , "orange" , "apple" , "mangoes" , "gava" , "sting" , "Coca-cola"]
print(x[1:])

# How to check if the item Exists in Lists
x = ["Banana" , "orange" , "apple" , "mangoes" , "gava" , "sting" , "Coca-cola"]
if "orange" in x:
    print("yes , 'orange' is in the list")

# Change the item value of the list
x = ["Banana" , "orange" , "apple" , "mangoes" , "gava" , "sting" , "Coca-cola"]
x[1] = "cake"
print(x)

# Change a Range of item values in lists
x = ["Banana" , "orange" , "apple" , "mangoes" , "gava" , "sting" , "Coca-cola"]
x[1:4] = ["gava" , "sting" , "Coca-cola"]
print(x)

# Change of one value by replacing it with 2 values
x = ["Banana" , "orange" , "apple" , "mangoes" , "gava" , "sting" , "Coca-cola"]
x[1:2] = ["Hamming","Elephant"]
print(x)
print(len(x))

# Change of two value by replacing it with 1 values
x = ["Banana" , "orange" , "apple" , "mangoes" , "gava" , "sting" , "Coca-cola"]
x[1:3] = ["Cherry"]
print(x)
print(len(x))


#__________________BEST OF LUCK ____________________#