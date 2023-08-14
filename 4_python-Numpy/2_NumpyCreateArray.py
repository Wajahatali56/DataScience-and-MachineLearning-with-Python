
# Now we will create a numpy nd-array object
#the array object in numpy is call nd-array
#array()
import numpy as np
x = np.array([1 , 2 ,3 ,4 , 5])
print(x)
print(type(x))

# we can also pass a list , tuple or any array like object with array(), and it will be converted to nd-array.

import numpy as np
y = np.array((1,2,3,4,5))
print(y)
print(type(y))

# Dimension in Arrays- a dimension in array is one level of array depth (nested array)

# 0-D Arrays - scalars , are  the elements in an array,each value in an array is a zero-D array.

# Now we will create 0-d array with value 42

import numpy as np
x = np.array(42)
print(x)

# 1-D array - an array that has 0-D arrays as its elements is called uni directional or 1-D.

import numpy as np
myarr =np.array([1, 2, 3, 4, 5])
print(myarr)

# Create a 2-D array containing 2 arrays with certain values.

import numpy as np
mycode = np.array([[1,2, 3, 4] , [7 , 8, 9 , 10]])
print(mycode)

# Now we will create a 3-D array with two 2-D array.

import numpy as np
mynum = np.array([[[1, 2, 3] , [5 , 6, 7]] , [[9 , 10 , 11] ,[11 , 12 , 13]]])
print(mynum)

# Check how many dimensions the array have : ndim attribute

import numpy as np
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1,2, 3, 4] , [7 , 8, 9 , 10]])
d = np.array([[[1, 2, 3] , [5 , 6, 7]] , [[9 , 10 , 11] ,[11 , 12 , 13]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Craete a array with 5 dimensions  and verify it has 5 dimensions.

import numpy as np
wajahat = np.array([1,2,3,4,5] , ndmin= 5)
print(wajahat)
print("Number of dimensions : " , wajahat.ndim)


#__________________BEST OF LUCK ____________________#