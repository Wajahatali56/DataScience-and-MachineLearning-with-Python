
# Defination of Dictionary: it is a key : value pair 

x = {
    "brand":"Tesla",
    "Model":"7T",
    "Year":2002
}
print(x)

# If you want to print "brand" value from the dict

x = {
    "brand":"Tesla",
    "Model":"7T",
    "Year":2002
}
print(x["brand"])

# Duplicate not allow , it will be overided 

x = {
    "brand":"Tesla",
    "Model":"7T",
    "Year":2002,
    "Model":"8t"
}
print(x)

# How to find dict length
x = {
    "brand":"Tesla",
    "Model":"7T",
    "Year":2002,
    "Model":"8t"
}
print(len(x))

# Dictionary items - Data types (multiple data types using)

x = {
    "brand":"Tesla",
    "Model":"7T",
    "Year":2002,
    "color":["white","blue","green"]
}
print(x)

# How to know the type of function
x = {
    "brand":"Tesla",
    "Model":"7T",
    "Year":2002,
    "color":["white","blue","green"]
}
print(type(x))

# Accessing items of Dict
x = {
    "brand":"Tesla",
    "Model":"7T",
    "Year":2002,
    "color":["white","blue","green"]
}
y = x["color"]
print(y)

# Accessing items of Dict through get() method
x = {
    "brand":"Tesla",
    "Model":"7T",
    "Year":2002,
    "color":["white","blue","green"]
}
y = x.get("color")
print(y)

# Key() methods will return all the keys in dict

x = {
    "brand":"Tesla",
    "Model":"7T",
    "Year":2002,
    "color":["white","blue","green"]
}
y = x.keys()
print(y) 

# Adding key and values items to the original dict
x = {
    "brand":"Tesla",
    "Model":"7T",
    "Year":2002,
}
y = x.keys()
print(y) # Before change
x["light"] = "Red"
print(x) # After change 


# values() methods will return all the values in dict

x = {
    "brand":"Tesla",
    "Model":"7T",
    "Year":2002,
    "color":["white","blue","green"]
}
y = x.values()
print(y) 

# Adding key and values items to the original dict
x = {
    "brand":"Tesla",
    "Model":"7T",
    "Year":2002,
}
y = x.values()
print(y) # Before change
x["light"] = "blue"
print(x) # After change 

# How to get items in a dict as tuples in the list
x = {
    "brand":"Tesla",
    "Model":"7T",
    "Year":2002,
    "color":["white","blue","green"]
}
y = x.items()
print(y)

# Check if key exists
x = {
    "brand":"Tesla",
    "Model":"7T",
    "Year":2002,
    "color":["white","blue","green"]
}
if "Year" in x:
    print("yes , 'Year' is present in x ")
    

#__________________BEST OF LUCK ____________________#