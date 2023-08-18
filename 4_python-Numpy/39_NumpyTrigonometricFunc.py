
# Trigonometric function: numpy provides the universal function like sin() , cos() and tan() that takes values in radians and produce the corresponding sin, cos and tan values.

# Here now we will find the sin value of pi/2:
import numpy as np
x1 = np.sin(np.pi/2)
print(x1)

# We will find the sin values of an array:

import numpy as np
x1 = np.array([np.pi/2 , np.pi/3 , np.pi/4 , np.pi/5])
xnew = np.sin(x1)
print(xnew)

# Convert degree into radians: by default all of the trig func takes radians as parameter.
#note:radians values pi/180* degree value.
# here we will convert all the array values to radians:

import numpy as np
x1 =np.array([90 , 180 , 270 , 360])
xnew = np.deg2rad(x1)
print(xnew)

# Convert radian into degree:

import numpy as np
x1 = np.array([np.pi/2 , np.pi ,1.5*np.pi , 2*np.pi])
xnew = np.rad2deg(x1)
print(xnew)

#here we can also find angels : arcsin() arccos() and arctan():
# we will now find the angel of 1.0:
import numpy as np
x1 = np.arcsin(1.0)
print(x1)

# angels of each values in an arrays:

import numpy as np
x1 = np.array([1 ,-1 , 0.1])
xnew = np.arcsin(x1)
print(xnew)

# Here we can also find the hypotaneous using the pythagoras theorem in numpy.
# hypot() func that takes values in radian and produce the corresponding sin , cos , tan values.
# here we will find the hypot for 3 base and 3 perpendicular.

import numpy as np
base = 3
perp = 4
x = np.hypot(base , perp)
print(x)


#__________________BEST OF LUCK ____________________#