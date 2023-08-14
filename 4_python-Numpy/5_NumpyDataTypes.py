
# Data types in python : string , integer , float , boolean , complex

# Data-types in Numpy
'''
i for integer
b for boolean
u for unsigned integer
f for float
c for complex
m for timedelta
M for datetime
O for object
S for string
U for unicode string
V - memory allocation

'''
# checking the data type of numpy array - dtype:

import numpy as np
xyz = np.array([1 , 2 , 3  , 4])
print(xyz.dtype)

# checking the data type of numpy array - string:

import numpy as np
xyz = np.array(["apple","banana"," cherry"])
print(xyz.dtype)

# Creating array with a defined data type:

import numpy as np
xyz = np.array([1 , 2 , 3  , 4] , dtype= 'S')
print(xyz)
print(xyz.dtype)

# Now we will create an array with data type of 4 byte int
import numpy as np
xyz = np.array([1 , 2 , 3  , 4] , dtype= 'i4')
print(xyz)
print(xyz.dtype)

# if a type is given in which the elements cannot be casted then numpy will raise error, what if a value cannot be converted?
# This code generates an error due to code incorrection example
'''
import numpy as np
xyz = np.array(['a' , '2' , '3' ] , dtype= 'i')
print(xyz.dtype) '''

# Converting data type in existing array - astype()

import numpy as np
xyz = np.array([1.1 , 2.3 , 5.7 , 8.9 ] )
xnew = xyz.astype('i') # you also write int for converting into (int)
print(xnew)
print(xnew.dtype)

# for Converting float
import numpy as np
xyz = np.array([1 , 2, 5 , 8] )
xnew = xyz.astype('f') # you also write float for converting into (float)
print(xnew)
print(xnew.dtype)


#__________________BEST OF LUCK ____________________#