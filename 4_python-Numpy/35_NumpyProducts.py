
# Products : use prod() function.

#Here we will find the product of the elements of the below array:

import numpy as np
x = np.array([1 , 2 , 3 , 4 , 5])
xnew = np.prod(x)
print(xnew)

# Here wwe will find product of elements in 2 different arrays:

import numpy as np
x1 = np.array([1 , 2 , 3 , 4 , 5]) # 1*2*3*4*5*1*2*3*4*5 = 14,400
x2 = np.array([1 , 2 , 3 , 4 , 5]) 
xnew = np.prod([x1 , x2])
print(xnew)

# Product over an axis:

import numpy as np
x1 = np.array([1 , 2 , 3 , 4 , 5]) # 1*2*3*4*5*1*2*3*4*5 = 14,400
x2 = np.array([1 , 2 , 3 , 4 , 5]) 
xnew = np.prod([x1 , x2] , axis=1)
print(xnew)

# Comulative product:

import numpy as np
x1 = np.array([1 , 2, 3 , 4 ,5])
xnew = np.cumprod(x1)
print(xnew)  


#__________________BEST OF LUCK ____________________#