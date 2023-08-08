
# JSON(javascript object notation) : is a syntex in which we store and exchange the data . 

# Converting from JSON to python
import json
x = '{"name" : "Ali" , "age" :30 , "subject":"Bs IT"}'
y = json.loads(x)
print(y["age"])

# Converting from python to JSON
import json
x = {"name" : "Ali" , "age" :30 , "subject":"Bs IT"}
y = json.dumps(x)
print(y)
print(type(y))

# You can convert the following python object to json string:
# dict , list , tuple , string , float , int , none , true , false
import json
print(json.dumps({"name" : "Ali" , "age" :30 }))
print(json.dumps(["apple" , "kiwi"]))
print(json.dumps(("wajahat" , "ali")))
print(json.dumps("Programmer"))
print(json.dumps(20))
print(json.dumps(20.16))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# When you convert from python to json than python object are converted into js json

import json
x = {"name" : "Ali" , "age" :30 , 
"married" :False , "study" : True , 
"children" : ("Haider" , "Ali") , "pets":None , 
"cars" : [{"Model" :"bmw" , "price" :2000000.00} , {"Model" :"frari" , "price" :900000.00}]} 

# Converting into json
y = json.dumps(x)
print(y)

# How to format result
import json
x = {"name" : "Ali" , "age" :30 , 
"married" :False , "study" : True , 
"children" : ("Haider" , "Ali") , "pets":None , 
"cars" : [{"Model" :"bmw" , "price" :2000000.00} , {"Model" :"frari" , "price" :900000.00}]} 

# Use the 4 indents to make code easy to read
print(json.dumps(x , indent=4))

# You can also define the separators meaning comma , colon space:

import json
x = {"name" : "Ali" , "age" :30 , 
"married" :False , "study" : True , 
"children" : ("Haider" , "Ali") , "pets":None , 
"cars" : [{"Model" :"bmw" , "price" :2000000.00} , {"Model" :"frari" , "price" :900000.00}]} 
print(json.dumps(x , indent=4 ,separators=("." , "=")))

# You can also get the result in specified order

import json
x = {"name" : "Ali" , "age" :30 , 
"married" :False , "study" : True , 
"children" : ("Haider" , "Ali") , "pets":None , 
"cars" : [{"Model" :"bmw" , "price" :2000000.00} , {"Model" :"frari" , "price" :900000.00}]} 
print(json.dumps(x , indent=4 ,sort_keys=True , separators=("." , "=")))


#__________________BEST OF LUCK ____________________#

