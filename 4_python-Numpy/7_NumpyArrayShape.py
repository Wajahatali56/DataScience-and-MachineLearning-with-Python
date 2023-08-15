
# Shape of an array - the shape of an array is the number of elements in each dimensions.

# Now we will try to get the shape of any array:

import numpy as np
ali = np.array([[1, 2 ,3 ,4 ,5] ,[6, 7 ,8 ,9 ,10]])
print(ali.shape)

# (2 , 5) which means array has 2 dimensions and it has 5 elements.
# Using 5-D array:
import numpy as np
wajahat = np.array([1,2,3,4,5] , ndmin= 5)
print(wajahat)
print("shape of array is : " , wajahat.shape)

#__________________BEST OF LUCK ____________________#