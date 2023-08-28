
# Scatter plot : A scatter plot is a diaghram where each value in the data set represented by the Dots.

#it is basicaly needs 2 array of the same length one for x-axis and other for y-axis.

# In below example x array represent the age of each car and the y array represent the speed of each car:

import matplotlib.pyplot as plt
x = [5 ,4 , 6 , 17 ,6 , 86 , 45 , 34 ,3 , 67, 8,6 ,4]
y = [99 , 86 , 87 , 98 , 64 , 95 , 29 , 101 , 56 , 90 , 80 , 90 , 95]
plt.scatter(x , y)
plt.show()

# Now we will do the above via random data dist - lets creates 2 array that are both filled with 1000 random numbers from normal data dist , the 1st array will have the mean set 5.0 with standard deviation of 1.0 , the 2nd array will have the mean set to 10.0 with SD of 2.0 :
import numpy as np
import matplotlib.pyplot as plt
x = np.random.normal(5.0 , 1.0 , 1000)
y  = np.random.normal(10.0 , 2.0 , 1000)
plt.scatter(x , y)
plt.show()



#__________________BEST OF LUCK __________________#