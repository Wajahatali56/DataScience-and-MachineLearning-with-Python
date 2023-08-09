# Linestyle or ls - is used to change the style of the plotted line

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3 ,8 , 1 , 10])
plt.plot(ypoints,linestyle = "dotted" ,marker ='o')
plt.show() 


# line color - c

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3 ,8 , 1 , 10])
plt.plot(ypoints,color = "r" ,marker ='o')
plt.show()


# Using Color-code like (#4CAF50)

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3 ,8 , 1 , 10])
plt.plot(ypoints,color = "#4CAF50" ,marker ='o')
plt.show()


# line width - lw .. width of line

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3 ,8 , 1 , 10])
plt.plot(ypoints,linewidth = '20' ,marker ='o')
plt.show() 

# Example for multiple line
import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([4 ,2, 12 , 8])
ypoints = np.array([3 ,8 , 1 , 10])
plt.plot(xpoints)
plt.plot(ypoints)
plt.show()


#__________________BEST OF LUCK ____________________#