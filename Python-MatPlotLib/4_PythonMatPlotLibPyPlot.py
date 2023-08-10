
 # now the pyplot package can be referred to as plt.
import matplotlib.pyplot as plt
import numpy as np

#plotting x and y
#plot() function is used to draw points or markers in a diagram.
#there are 2 parameters for specifying points in the diaghram i.e x-axis & y -axis.

xpoints =np.array([1,8])
ypoints =np.array([2,10])
plt.plot(xpoints , ypoints)
plt.show()

# the x-axis is the horizontal axis
# the y-axis is the vertical axis

import matplotlib.pyplot as plt
import numpy as np

xpoints =np.array([1,8])
ypoints =np.array([2,10])
plt.plot(xpoints , ypoints , 'o') # it just show two dotted points on graph
plt.show() 

import matplotlib.pyplot as plt
import numpy as np

xpoints =np.array([1, 2, 6 , 8])
ypoints =np.array([3 , 8, 1,10])
plt.plot(xpoints , ypoints ) 
plt.show()

# Default x-points:
import matplotlib.pyplot as plt
import numpy as np
ypoints =np.array([2, 12, 8, 9 ,10, 5])
plt.plot(ypoints ) 
plt.show()

#__________________BEST OF LUCK ____________________#