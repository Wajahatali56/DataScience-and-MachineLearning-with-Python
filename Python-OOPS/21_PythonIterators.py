# An iterator is an object which implements the iterators protocol, which consist of two methods:__iter__() and __next__()
# iterators vs iterables

tuple1 = ("apple" , "banana" ,"cherry")
newtuple = iter(tuple1)
print(next(newtuple))
print(next(newtuple))
print(next(newtuple))

# another example

x = "apple"
y = iter(x)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))

# looping through an iterators


tuple1 = ("apple" , "banana" ,"cherry")
for i in tuple1:
    print(i)

# looping through a string as iterators 
x = "apple"
for i in x:
    print(i)

# Create an iterators : to create an object and class you will have to implement __iter__() and __next__() to the object.



