# RegEx : Regular Expression , is a sequence of characters that forms a search pattern.
import re
txt = "what are you doing here tell me why"
x = re.search("^what.*why$",txt )
if x:
    print("Yes , match is true")
else:
    print("No match")

# RegeX functions
#findall
#search()
#split()
#sub()

# Metacharacters
# \d - escape character
# . - any character(except newline character)
# ^ - start with
# $ - Ends with
# * - zero or more occurence
# + - one or more occurence
# ? - zero or one occurence
# {} - Exactly the specified number of occurence
# | - Either or
#() -capture and group

#the findall() function
import re
string = "My name is wajahat"
x = re.findall("a" , string)
print(x)

# If in find all no condition is given than it will show empty list.

import re
string = "My name is wajahat"
x = re.findall("or" , string)# or is not present in string
print(x)

#the search() function
import re
string = "My name is wajahat"
x = re.search("\s" , string)
print("white space is located in",x.start())

# when nothing found in search() function
import re
string = "My name is wajahat"
x = re.search("ali" , string)
print(x)

# the split() function

import re
string = "My name is wajahat"
x = re.split("\s" , string)
print(x)

# You can control number of occurance by specifying the maxsplit parameter.

import re
string = "My name is wajahat"
x = re.split("\s" , string , 2)
print(x)

#the sub() function - replace the matches with the text of your choice 

import re
string = "My name is wajahat"
x = re.sub("\s" , "56" ,string)
print(x)

# You can control the number of replace ment by specifying the count parameter
import re
string = "My name is wajahat"
x = re.sub("\s" , "56" ,string , 2)
print(x)

#__________________BEST OF LUCK ____________________#


