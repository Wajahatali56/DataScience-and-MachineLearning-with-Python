
# Loop through the dict

x = {
    "brand":"Tesla",
    "Model":"xyz",
    "Year":"2002"
}
for i in x:
    print(i)

# With looping print all values of key in the dict one by one 
x = {
    "brand":"Tesla",
    "Model":"xyz",
    "Year":"2002"
}
for i in x:
    print(x[i])

# Value() method is used to return values of the dict
x = {
    "brand":"Tesla",
    "Model":"xyz",
    "Year":"2002"
}
for i in x.values():
    print(i)

# keys() method is used to return keys of the dict
x = {
    "brand":"Tesla",
    "Model":"xyz",
    "Year":"2002"
}
for i in x.keys():
    print(i)

# Now loop through both the keys and values , by using the items() method
x = {
    "brand":"Tesla",
    "Model":"xyz",
    "Year":"2002"
}
for i , y in x.items():
    print(i , y)

# How to copy the dict

x = {
    "brand":"Tesla",
    "Model":"xyz",
    "Year":"2002"
}
y = x.copy()
print(y)

# Another way to make a copy using dict() - built in function

x = {
    "brand":"Tesla",
    "Model":"xyz",
    "Year":"2002"
}
y = dict(x)
print(y)

# Nested Dict :  A dictionary can able to contain an another dictionary

myfamily = {
    "child1": {
         "Name":"Ali",
         "Age":23   
    },
    "child2": {
         "Name":"Hurray",
         "Age":20   
    },
    "child3": {
         "Name":"Python",
         "Age":30   
    }
   
}
print(myfamily)

# If you want to add 3 dict into a new dict.

child1=  {
         "Name":"Ali",
         "Age":23   
    },
child2= {
         "Name":"Hurray",
         "Age":20   
    },
child3 =  {
         "Name":"Python",
         "Age":30   
    }
   
myfamily = {
    "child1":child1,
    "child2":child2,
    "child3":child3
}

print(myfamily)
'''
# Python dict Method()
clear()
copy()
get()
items()
keys()
fromkeys()
pop()
popitem()
update()
values()
setdefault...

'''


#__________________BEST OF LUCK ____________________#