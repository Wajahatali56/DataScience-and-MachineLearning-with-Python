
# Summations : difference is that addition is done btw 2 arg* whereas summation happens over n elements.

# adding the 2 arrays:
import numpy as np
x1 = np.array([1 , 2, 3])
x2 = np.array([1 , 2 , 3])
xnew = np.add(x1 , x2)
print(xnew)

# Sum the values in 2 array:

import numpy as np
x1 = np.array([1 , 2, 3])
x2 = np.array([1 , 2 , 3])
xnew = np.sum([x1 , x2])
print(xnew)

# summation over an exist : if you specify axis=1 , numpy will sum the number in each array :

import numpy as np
x1 = np.array([1 , 2, 3])
x2 = np.array([1 , 2 , 3])
xnew = np.sum([x1 , x2] , axis=1)
print(xnew)

# commulative sum: means partially adding the element in array:
#Example : [1 , 2 , 3 ,4] would be [1 1+2 1+2+3 1+2+3+4 ] = [1 3 6 10] represent by cumsum():

import numpy as np
x1 = np.array([1 , 2, 3 , 4])
xnew = np.cumsum(x1)
print(xnew)


#__________________BEST OF LUCK ____________________#
