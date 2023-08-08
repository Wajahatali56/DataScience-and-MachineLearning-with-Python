
# What are sets (unordered , unchangeable , unindexed)
x = {"apple" , "banana" , "kiwi" , "orange"}
print(x)

# Duplicate not allowed 
x = {"a" , "b" , "c" , "c" , "a"}
print(x)

# get the lenght of sets
x = {"apple" , "banana" , "kiwi" , "orange"}
print(len(x))

# Check the data type of sets 
set1 = {"a" , "b" , "c"}
set2 = {1 , 4 , 7 , 9}
set3  = {True , False , True}
print(set1)
print(set2)
print(set3)
print(type(set1))
print(type(set2))
print(type(set3))

# A set with string , integer and Boolean means all data types 
set1 = {4 , "orange" , 2.5 , True , True}
print(set1)

# The set Constructor
conset = set((4 , "orange" , 2.5 , True , True))
print(conset)

# How to access items in sets 
accset = {"a" , "b" ,"c"}
for i in accset:
    print(i)

# Check if "banana" is present in set or not

x = {"apple" , "banana" , "kiwi" , "orange"}
print("banana" in x)

# Adding set items
x = {"apple" , "banana" , "kiwi" , "orange"}
x.add("soap")
print(x)

# How to add items from another set into the current set by update()methode
x = {"apple" , "banana" , "kiwi" , "orange"}
y = {"a" , "b" ,"c"}
x.update(y)
print(x)

# Removing set items
x = {"apple" , "banana" , "kiwi" , "orange"}
x.remove("kiwi")
print(x)

# discard() set items
x = {"apple" , "banana" , "kiwi" , "orange"}
x.discard("kiwi")
print(x)

# remove the last item by using pop() method will raise the error or you will get the wrong output 
x = {"apple" , "banana" , "kiwi" , "orange"}
y = x.pop()
print(y)
print(x)

# Clear() method is used for empty the set

x = {"apple" , "banana" , "kiwi" , "orange"}
x.clear()
print(x)

# Del keyword is used to delete the set completely
x = {"apple" , "banana" , "kiwi" , "orange"}
del x

# How to use loop in sets
x = {"apple" , "banana" , "kiwi" , "orange"}
for i in x:
    print(i)

# Joining two sets by union() and update()

x = {"apple" , "banana" , "kiwi" , "orange"}
y = {1 , 2 , 4 , 9 , 10}
z = x.union(y)
print(z)

# update() using

x = {"apple" , "banana" , "kiwi" , "orange"}
y = {1 , 2 , 4 , 9 , 10}
x.update(y)
print(x)

# Use intersection which allow duplicate value
x = {"apple" , "banana" , "kiwi" , "orange"}
y = {"apple" , "banana" , "kiwi" }
x.intersection_update(y)
print(x)

x = {"apple" , "banana" , "kiwi" , "orange"}
y = {"apple" , "banana" , "kiwi" }
z = x.intersection(y)
print(z)

# keep all , but not the duplicate or common value

x = {"apple" , "banana" , "kiwi" , "orange"}
y = {"apple" , "banana" , "kiwi" }
x.symmetric_difference_update(y)
print(x)

# Symmetric_difference() method eill return a new set that contain only the element that are not present in Both sets

x = {"apple" , "banana" , "kiwi" , "orange"}
y = {"apple" , "banana" , "kiwi" }
z = x.symmetric_difference(y)
print(z)

'''
# All Built_in Sets Methods in python
add()
clear()
copy()
difference()
difference_update()
discard()
intersection()
intersection_update()
pop()
update()
remove()
union()
symmetric_difference()
symmetric_difference_update()

'''

#__________________BEST OF LUCK ____________________#