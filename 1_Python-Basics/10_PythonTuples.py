
x = ("banana" , "orange" , "apple" , "mangoes")
print(type(x))

# Tuple length

x = ("banana" , "orange" , "apple" , "mangoes")
print(len(x))

# Create tuple with one item

x = ("python",)
print(type(x))

# Not a tuple 

x = ("python") # Its read as a string
print(type(x))

# tuple items - data types (str , int , boolean)

x = ("banana" , "orange" , "apple" , "mangoes")
y = (1 , 2 , 4 , 9 , 10)
z = (True , False , True)
print(x)
print(y)
print(z)

# tuples can also contains different datatypes
 
x = ("banana" , 12 , True , 20 , "mangoes" , False)
print(x)

# The tuple constructor 
x = tuple(("banana" , "orange" , "apple" , "mangoes"))
print(x)
print(type(x))

# Access tuples items 
x = ("banana" , "orange" , "apple" , "mangoes")
print(x[3])

# access tuples item through negative indexing 

x = ("banana" , "orange" , "apple" , "mangoes")
print(x[-1])

# access tuples item through range of indexes

x = ("banana" , "orange" , "apple" , "mangoes" , "wajahat" , "ali" , "opera-mini" , "pandas" , "series")
print(x[2:7]) # last item not included

# access tuples item through range of indexes but some index not included

x = ("banana" , "orange" , "apple" , "mangoes" , "wajahat" , "ali" , "opera-mini" , "pandas" , "series")
print(x[:8])

x = ("banana" , "orange" , "apple" , "mangoes" , "wajahat" , "ali" , "opera-mini" , "pandas" , "series")
print(x[1:])

# access tuples item through negative range of indexes

x = ("banana" , "orange" , "apple" , "mangoes" , "wajahat" , "ali" , "opera-mini" , "pandas" , "series")
print(x[-5:-1]) # -1 is not included as positive indexing

# check if the item exits 
x = ("banana" , "orange" , "apple" , "mangoes" , "wajahat" , "ali" , "opera-mini" , "pandas" , "series")
if "pandas" in x:
    print("yes ,'pandas' is in x")

# Changing in tuple values (* 007)
x = ("banana" , "orange" , "apple" , "mangoes" , "wajahat" , "ali" , "opera-mini" , "pandas" , "series")
print(type(x))
y = list(x)
print(type(y))
y[3] = "Wajahat-Engineer"
x = tuple(y)
print(x)
print(type(x))

# Add items in tuple values (* 007)

x = ("banana" , "orange" , "apple" , "mangoes" , "wajahat" , "ali" , "opera-mini" , "pandas" , "series")
print(type(x))
y = list(x)
print(type(y))
y.append("wajahatatlast")
x = tuple(y)
print(x)

# Adding tuple to a tuple
x = ("banana" , "orange" , "apple" , "mangoes")
y = ("wajahatdeveloper",)
x += y
print(x)

# Removing items from a tuples 

x = ("banana" , "orange" , "apple" , "mangoes" , "wajahat" , "ali" , "opera-mini" , "pandas" , "series")
print(type(x))
y = list(x)
print(type(y))
y.remove("series")
x = tuple(y)
print(x)
print(type(x))

# how to delete tuple 
x = ("banana" , "orange" , "apple" , "mangoes" , "wajahat" , "ali" , "opera-mini" , "pandas" , "series")
del x 

# Packing a tuple (when we assign a value to tuple)
x = ("Wajahat" , "ali" , "python" , "result")

# Unpacking a tuple (when we extract a value from tuple)
x = ("Wajahat" , "ali" , "python" , "result")
(a , b , *c) = x
print(a)
print(b)
print(c)



#__________________BEST OF LUCK ____________________#











