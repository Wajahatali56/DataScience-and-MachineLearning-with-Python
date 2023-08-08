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
# All classes have a function which is called __init__().
# which allow you to do some initialization.

# Example for better understanding :
class mynumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
myclass = mynumber()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# stopiteration : to prevent the iteration to go over forever ,we use the stopiteration statement 

class mynum:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass = mynum()
myiter = iter(myclass)
for i in myiter:
    print(i)


#__________________BEST OF LUCK ____________________#