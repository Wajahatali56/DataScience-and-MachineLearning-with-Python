
# Getting some elements out of an existing array and creating a new array called filtering.

# A boolean index list is a list of boolean corresponding to indexes in the array.(True and False)

# Create an array from the element on index 0 to 2:
import numpy as np
wajahat =np.array([41 , 42 , 43 , 44])
newarr =[True , False , True , False]
finalarray =wajahat[newarr]
print(finalarray) 
print('**************************')
# Now we will create a filter array - that will return only values higher than 42:

import numpy as np
wajahat =np.array([41 , 42 , 43 , 44])
emptyarr =[]
for i in wajahat:
    if i > 42: # i represent elements in arr
        emptyarr.append(True)
    else:
        emptyarr.append(False)
newwajahat =wajahat[emptyarr]
print(emptyarr)
print(newwajahat)
print('**************************')
# Create a filter array that will return only even elements from the original array:

import numpy as np
wajahat = np.array([1 , 2, 3, 4, 5 ,6 , 7 , 8 ,9])
emptywajahat=[]
for i in wajahat:
    if i%2 == 0:
        emptywajahat.append(True)
    else:
        emptywajahat.append(False)
finalarr = wajahat[emptywajahat]
print(emptywajahat)
print(finalarr)
print('**************************')
# You can also create filter directly from array:

import numpy as np
wajahat =np.array([41 , 42 , 43 , 44])
emptywajahat = wajahat > 42
newwajahat = wajahat[emptywajahat]
print(emptywajahat)
print(newwajahat)
print('**************************')

# Alternate method to print even numbers

import numpy as np
wajahat = np.array([1 , 2, 3, 4, 5 ,6 , 7 , 8 ,9])
emptywajahat=wajahat%2 == 0 
finalarr = wajahat[emptywajahat]
print(emptywajahat)
print(finalarr)

#__________________BEST OF LUCK ____________________#