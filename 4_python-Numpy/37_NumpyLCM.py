
# Finding LCM(lowest common Multiplication)
# Here we will find the LCM of the 2 numbers:

import numpy as np
x = 4
y = 6
znew = np.lcm(x , y)
print(znew)

# Finding the LCM in array:
import numpy as np
x1 = np.array([3 , 6 , 9])# the reduce() method will use the ufunc , in this case the lcm() function on each elements and it will reduce the array by 1 dimension.
xnew = np.lcm.reduce(x1)
print(xnew)

# Here we will find the LCM of all of an array where array contains all integers from 1 to 10:

import numpy as np
x1 = np.arange(1 , 11)
xnew = np.lcm.reduce(x1)
print(xnew)


#__________________BEST OF LUCK ____________________#