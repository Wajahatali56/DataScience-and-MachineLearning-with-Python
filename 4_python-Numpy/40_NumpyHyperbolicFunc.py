
# hyperbolic function: numpy provides the universal function like sinh() , cosh() and tanh() that takes values in radians and produce the corresponding sin, cos and tan values.

# Here we will find the value of sinh of pi/2:
import numpy as np
x1 = np.sinh(np.pi/2)
print(x1)

# we will find cosh values in array:

import numpy as np
x1 = np.array([np.pi/2 , np.pi/3 , np.pi/4 , np.pi/5])
xnew = np.cosh(x1)
print(xnew)

#here we can also find angels : arcsinh() arccosh() and arctanh():
# we will now find the angel of 1.0:
import numpy as np
x1 = np.arcsinh(1.0)
print(x1)

# angels of each tanh values in an arrays:

import numpy as np
x1 = np.array([0.1 , 0.2 , 0.5])
xnew = np.arctanh(x1)
print(xnew)



#__________________BEST OF LUCK ____________________#