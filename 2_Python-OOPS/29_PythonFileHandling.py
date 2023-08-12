
# File handling - open()

file = open("C:\\Users\\USER PC\\DATA SCIENCE with PYTHON\\Python-OOPS\\testfile.txt")

# or
f = open('C:\\Users\\USER PC\\DATA SCIENCE with PYTHON\\Python-OOPS\\testfile.txt' , "rt") # rt = read text
 
# there are 4 different modes of opening file
# "r"  , "a" , "w" , "x" x for error

# To open a file using built in open() and read()
# open a file in different location
x = open("C:\\Users\\USER PC\\DATA SCIENCE with PYTHON\\Python-OOPS\\testfile.txt" , "r")
print(x.read())
print("***************")
# open a file in different location

f = open("C:\\Users\\USER PC\\DATA SCIENCE with PYTHON\\Python-OOPS\\testfile.txt", "r")
print(f.read())
print("***************")
# read only parts of the file
f = open("C:\\Users\\USER PC\\DATA SCIENCE with PYTHON\\Python-OOPS\\testfile.txt", "r")
print(f.read(7))
print("***************")
# How to read lines 
f = open("C:\\Users\\USER PC\\DATA SCIENCE with PYTHON\\Python-OOPS\\testfile.txt", "r")
print(f.readline())
print(f.readline())
print("***************")
# Looping through the line by line:
f = open("C:\\Users\\USER PC\\DATA SCIENCE with PYTHON\\Python-OOPS\\testfile.txt", "r")
for i in f:
    print(i)
print("***************")
# How to close the open file:

f = open("C:\\Users\\USER PC\\DATA SCIENCE with PYTHON\\Python-OOPS\\testfile.txt", "r")
print(f.readline())
f.close()
print("***************")

#__________________BEST OF LUCK ____________________#