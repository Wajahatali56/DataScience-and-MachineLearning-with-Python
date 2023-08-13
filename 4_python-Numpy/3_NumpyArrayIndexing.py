
# Array indexing is the same as accessing an array elements.
# Indexing Start with 0 always , second is 1
import numpy as np
ali = np.array([1, 2 ,3 ,4 ,5])
print(ali[0])

# we can get the third and forth elements from adding them:

import numpy as np
ali = np.array([1, 2 ,3 ,4 ,5])
print(ali[2] + ali[3])

# Accessing the 2-D - it is like a rows and columns.

import numpy as np
ali = np.array([[1, 2 ,3 ,4 ,5] ,[6, 7 ,8 ,9 ,10]])
# print("2nd element in the 1st row :" , ali[0 , 1]) 

print("5th element in the 2nd row :" , ali[1, 4]) # it will show : 10

# Accessing the 3-D
import numpy as np
wajahat = np.array([[[1 , 2, 3] , [5 , 6 , 7]]  , [[10 , 11, 13] , [15 , 16 , 17]]])

print(wajahat[1 , 1 , 2]) # it will show : 17


#__________________BEST OF LUCK ____________________#