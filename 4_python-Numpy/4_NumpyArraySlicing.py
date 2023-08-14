
# Slicing Array- slicing in python means taking elements from one given index to another index.
# [start : end] , [start:end:step]
# Now we will slice an elements from 1 to 5:

import numpy as np
wajahat = np.array([1 , 2, 3, 4, 5 ,6, 7 , 8 , 9])
print(wajahat[1:5])

# Now we will slice from index 4 to the end value:

import numpy as np
wajahat = np.array([1 , 2, 3, 4, 5 ,6, 7 , 8 , 9])
print(wajahat[4:])

# Now we wil slice the element from the begining to index 4:

import numpy as np
wajahat = np.array([1 , 2, 3, 4, 5 ,6, 7 , 8 , 9])
print(wajahat[:4])

# Negative slicing - index 3 to end

import numpy as np
wajahat = np.array([1 , 2, 3, 4, 5 ,6, 7 , 8 , 9])
print(wajahat[-5:-1])

#Step : you will use step value to determine the step of the slicing.
# return every other value from index 1 to 5:

import numpy as np
wajahat = np.array([1 , 2, 3, 4, 5 ,6, 7 , 8 , 9])
print(wajahat[1:5:2]) # har dosra number

# Return every other number from the entire array:

import numpy as np
wajahat = np.array([1 , 2, 3, 4, 5 ,6, 7 , 8 , 9])
print(wajahat[::2]) 
# with [::3]
import numpy as np
wajahat = np.array([1 , 2, 3, 4, 5 ,6, 7 , 8 , 9])
print(wajahat[::3]) 

# Slicing with 2-D array-print 7,8,9

import numpy as np
ali = np.array([[1, 2 ,3 ,4 ,5] ,[6, 7 ,8 ,9 ,10]])
print(ali[1 , 1:4])

# Another example:

import numpy as np
ali = np.array([[1, 2 ,3 ,4 ,5] ,[6, 7 ,8 ,9 ,10]])
print(ali[0:2 , 2])

# Another Tough example:

import numpy as np
ali = np.array([[1, 2 ,3 ,4 ,5] ,[6, 7 ,8 ,9 ,10]])
print(ali[0:2 ,1:4])
print("*******************")
# 3-D slicing Example:

import numpy as np
wajahat = np.array([[[1 , 2, 3] , [5 , 6 , 7]]  , [[10 , 11, 13] , [15 , 16 , 17]]])
print(wajahat[0:4 , 0 , 1:3])

#__________________BEST OF LUCK ____________________#