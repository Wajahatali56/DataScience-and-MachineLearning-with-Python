
# Finding LCM(lowest common Multiplication)
# Here we will find the LCM of the 2 numbers:

import numpy as np
x = 4
y = 6
znew = np.lcm(x , y)
print(znew)

# Finding the LCM in array:
import numpy as np
x1 = np.array([3 , 6 , 9])
xnew = np.lcm.reduce(x1)
print(xnew)
