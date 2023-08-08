# Built-in datatypes:
'''Text type :str
Numeric type : int , float , complex 
sequence type : list , tuple ,range 
mapping : dict
set type: set , frozenset
boolean types : bool 
Binary types : bytes , bytearray , memoryview'''

x = 5
y = "wajahat ali"
print(type(x))
print(type(y))

x = 5 #int
x = "wajahat ali" #string
print(x)
x = 5.0 #float
x = 1j #complex
x = ["wajahat","Arshad"] #list
x = ("wajahat" , "Arshad") #tuple
x = range(10) #range
print(x)
x = {"Name" : "Wajahat" , "Age" : "20"} #dic
x = {"apple" , "Banana" , "Orange"} #set
x = True #bool
x = b"wajahat" #bytes
x = bytearray(5) #bytearray
x = memoryview(bytes(5)) # memoryview


# Setting out specific data types 

x = str("wajahat ali")
print(x)
x = int(5)
x = float(5.0)
x = complex(1j)
x = list(("apple" , "Banana" , "Orange"))
x = tuple(("apple" , "Banana" , "Orange"))
x = range(10)
x = dict(Name = "Wajahat" , Age = 20)
x = set(("apple" , "Banana" , "Orange"))
x = frozenset(("apple" , "Banana" , "Orange"))
x = bool(2)
x = bytes(23)
x = bytearray(10)
x = memoryview(bytes(5))


#__________________BEST OF LUCK ____________________#