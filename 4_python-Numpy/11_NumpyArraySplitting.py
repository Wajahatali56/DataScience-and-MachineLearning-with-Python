
# Splitting arrays in numpy - it is reverse to joining , breaking the array.

# array_split()

# Spli the array in 3 parts:
import numpy as np
wajahat = np.array([1,2,3,4,5,6])
wajahat1 = np.array_split(wajahat , 3)
print(wajahat1)
print('**************************')
# Now we will split this array in 4 parts:

import numpy as np
wajahat = np.array([1,2,3,4,5,6])
wajahat1 = np.array_split(wajahat , 4)
print(wajahat1)
print('**************************')
# Split into array with index:

import numpy as np
wajahat = np.array([1,2,3,4,5,6])
wajahat1 = np.array_split(wajahat , 3)
print(wajahat1[0])
print(wajahat1[1])
print(wajahat1[2])
('**************************')
# Splitting the 2-D array:

import numpy as np
arr = np.array([[1,2] , [3,4] , [5,6] ,[7,8],[9,10] , [11 , 12]])
newarr = np.array_split(arr,3)
print(newarr)
print('**************************')
# Split the 2-D array into three 2-D arrays:

import numpy as np
arr = np.array([[1,2 ,3] , [4 , 5 , 6] ,[7, 8 ,9 ] , [10 , 11 , 12], [13 , 14 , 15],[16 , 17 ,18]])
newarr = np.array_split(arr,3)
print(newarr)
print('**************************')

# Splitting the 2-D into three 2-D along with rows:

import numpy as np
arr = np.array([[1,2 ,3] , [4 , 5 , 6] ,[7, 8 ,9 ] , [10 , 11 , 12], [13 , 14 , 15],[16 , 17 ,18]])
newarr = np.array_split(arr,3 , axis=1)
print(newarr)
print('**************************')
# Alternate solution is using the hsplit() , opposite hstack() 

import numpy as np
arr = np.array([[1,2 ,3] , [4 , 5 , 6] ,[7, 8 ,9 ] , [10 , 11 , 12], [13 , 14 , 15],[16 , 17 ,18]])
newarr = np.hsplit(arr,3)
print(newarr)


#__________________BEST OF LUCK ____________________#