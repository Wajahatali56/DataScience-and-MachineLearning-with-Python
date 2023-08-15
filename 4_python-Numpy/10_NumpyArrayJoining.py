
# Joining the numpy array - here for this we will pass concatenate()

import numpy as np
wajahat = np.array([1,2,3])
wajahat1 = np.array([4,5,6])
newarray = np.concatenate((wajahat , wajahat1))
print(newarray)

# Joining of 2-D along with rows(axis-1):

import numpy as np
wajahat = np.array([[1,2,3] , [4,5,6]])
wajahat1 = np.array([[7,8,9] , [10 ,11, 12]])
newarr = np.concatenate((wajahat , wajahat1) , axis=1)
print(newarr)

# Joining array using the stack function:
import numpy as np
wajahat = np.array([1,2,3])
wajahat1 = np.array([4,5,6])
newarray = np.stack((wajahat , wajahat1) , axis= 1)
print(newarray)

# Stacking along with rows : hstacks() 
import numpy as np
wajahat = np.array([1,2,3])
wajahat1 = np.array([4,5,6])
newarray = np.hstack((wajahat , wajahat1))
print(newarray)

# Stacking along with columns:

import numpy as np
wajahat = np.array([1,2,3])
wajahat1 = np.array([4,5,6])
newarray = np.vstack((wajahat , wajahat1))
print(newarray)

# Stacking along with height(depth):

import numpy as np
wajahat = np.array([1,2,3])
wajahat1 = np.array([4,5,6])
newarray = np.dstack((wajahat , wajahat1))
print(newarray)


#__________________BEST OF LUCK ____________________#