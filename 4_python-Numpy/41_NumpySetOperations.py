
# What is set? a set is a collection of unique elements.

# For creating the set we use numpy's unique() to find the unique elements from an array.
# here we will convert the array with repeated elements to a set:
import numpy as np
x1 = np.array([1,1 , 2 , 2, 2, 2, 2, 2, 1 , 1, 1, 1,5 , 7, 8, 9, 4])
xnew =np.unique(x1)
print(xnew)

# to find the unique values of 2 1-D array , we will use union1d() method :

import numpy as np
x1 = np.array([1,2 , 7, 8, 9, 4])
x2 = np.array([1, 2 , 9])
xnew =np.union1d(x1 , x2)
print(xnew)

# to find the only values that are present in both array,we will use intersect1d() method.

import numpy as np
x1 = np.array([1,2 , 7, 8, 9, 4])
x2 = np.array([1, 2 , 9])
xnew =np.intersect1d(x1 , x2 , assume_unique=True)
print(xnew)

# to find the only values that are in 1st set and NOT present in the 2nd set - use setdiff1d():

import numpy as np
x1 = np.array([1,2 , 7, 8, 9, 4])
x2 = np.array([1, 2 , 9])
xnew =np.setdiff1d(x1 , x2 ,assume_unique=True)
print(xnew)

# to find the only values that are not present in both sets - setxor1d() method:

import numpy as np
x1 = np.array([1,2 , 7, 8, 9, 4])
x2 = np.array([1, 2 , 9 , 11])
xnew =np.setxor1d(x1 , x2)
print(xnew)


#__________________BEST OF LUCK ____________________#