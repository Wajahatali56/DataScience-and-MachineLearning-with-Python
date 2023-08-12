# 2 modes for writing in the file
# "a" , "w"
'''
f = open("C:\\Users\\USER PC\\DATA SCIENCE with PYTHON\\Python-OOPS\\testfile.txt", "a")
f.write("Now this file has been updated")
f.close()

# Open and read the file after appending:
f = open("C:\\Users\\USER PC\\DATA SCIENCE with PYTHON\\Python-OOPS\\testfile.txt", "r")
print(f.read())
'''
# 1st open the file and override the content.
f = open("C:\\Users\\USER PC\\DATA SCIENCE with PYTHON\\Python-OOPS\\testfile.txt", "w")
f.write("File has been overrided")
f.close()

# open and read the file after the appending
f = open("C:\\Users\\USER PC\\DATA SCIENCE with PYTHON\\Python-OOPS\\testfile.txt", "r")
print(f.read())

# Craeting a new file
# "x" for create a file
# "a" for append a file
# "w" for write or create in a file
f = open("myfile.txt" , "x")

# How to delete a file
import os
os.remove("myfile.txt")

# check if the file exist
import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("'myfile' not exist")

#  How to delete the existing folder
import os
os.rmdir("myfolder")# this commad can remove only empty folder

#__________________BEST OF LUCK ____________________#