
# Display the multiple plot - with subplot() you can draw multiple plots in one figure.

import matplotlib.pyplot as plt
import numpy as np

# plot1
x = np.array([0 , 1 , 2, 3])
y = np.array([3 , 8 ,1 ,10])
plt.subplot(1 , 2 , 1)# the figure has 1 row , 2 colums and this plot is the 1st plot.
plt.plot(x , y)

#plot2

x = np.array([0 , 1 , 2, 3])
y = np.array([10 , 20 ,30 ,40])
plt.subplot(1 , 2 , 2)
plt.plot(x , y)

plt.show()

# Now we will draw 2 plot on top of each others

import matplotlib.pyplot as plt
import numpy as np

# plot1
x = np.array([0 , 1 , 2, 3])
y = np.array([3 , 8 ,1 ,10])
plt.subplot(2 , 1 , 1)# the figure has 2 row , 1 colums and this plot is the 1st plot.
plt.plot(x , y)

#plot2

x = np.array([0 , 1 , 2, 3])
y = np.array([10 , 20 ,30 ,40])
plt.subplot(2 , 1 , 2)
plt.plot(x , y)

plt.show() 

# Now we will draw challenge of 6 plot (__________Best of luck_______)

import matplotlib.pyplot as plt
import numpy as np

# plot1
x = np.array([0 , 1 , 2, 3])
y = np.array([3 , 8 ,1 ,10])
plt.subplot(2 , 3 , 1)# the figure has 2 row , 3 colums and this plot is the 1st plot.
plt.plot(x , y)

# plot2
x = np.array([0 , 1 , 2, 3])
y = np.array([3 , 8 ,1 ,10])
plt.subplot(2 , 3 , 2)# the figure has 2 row , 3 colums and this plot is the 2nd plot.
plt.plot(x , y)

# plot3
x = np.array([0 , 1 , 2, 3])
y = np.array([3 , 8 ,1 ,10])
plt.subplot(2 , 3 , 3)# the figure has 2 row , 3 colums and this plot is the 3rd plot.
plt.plot(x , y)

# plot4
x = np.array([0 , 1 , 2, 3])
y = np.array([3 , 60,1 ,10])
plt.subplot(2 , 3 , 4)# the figure has 2 row , 3 colums and this plot is the 4th plot.
plt.plot(x , y)

# plot5
x = np.array([0 , 1 , 2, 3])
y = np.array([3 , 8 ,1 ,10])
plt.subplot(2 , 3 , 5)# the figure has 2 row , 3 colums and this plot is the 5th plot.
plt.plot(x , y)

# plot6
x = np.array([0 , 1 , 2, 3])
y = np.array([3 , 8 ,1 ,80])
plt.subplot(2 , 3 , 6)# the figure has 2 row , 3 colums and this plot is the 6th plot.
plt.plot(x , y)
plt.show()

# 6 plot with individual title name

import matplotlib.pyplot as plt
import numpy as np

# plot1
x = np.array([0 , 1 , 2, 3])
y = np.array([3 , 8 ,1 ,10])
plt.subplot(2 , 3 , 1)
plt.plot(x , y)
plt.title("sales")

# plot2
x = np.array([0 , 1 , 2, 3])
y = np.array([3 , 8 ,1 ,10])
plt.subplot(2 , 3 , 2)
plt.plot(x , y)
plt.title("Marketing")
# plot3
x = np.array([0 , 1 , 2, 3])
y = np.array([3 , 8 ,1 ,10])
plt.subplot(2 , 3 , 3)
plt.plot(x , y)
plt.title("Coding")
# plot4
x = np.array([0 , 1 , 2, 3])
y = np.array([3 , 60,1 ,10])
plt.subplot(2 , 3 , 4)
plt.plot(x , y)
plt.title("Patent")
# plot5
x = np.array([0 , 1 , 2, 3])
y = np.array([3 , 8 ,1 ,10])
plt.subplot(2 , 3 , 5)
plt.plot(x , y)
plt.title("Network")
# plot6
x = np.array([0 , 1 , 2, 3])
y = np.array([3 , 8 ,1 ,80])
plt.subplot(2 , 3 , 6)
plt.plot(x , y)
plt.title("sales Executive")
plt.show() 

# 6 plot with supertitle

import matplotlib.pyplot as plt
import numpy as np

# plot1
x = np.array([0 , 1 , 2, 3])
y = np.array([3 , 8 ,1 ,10])
plt.subplot(2 , 3 , 1)
plt.plot(x , y)
plt.title("sales")

# plot2
x = np.array([0 , 1 , 2, 3])
y = np.array([3 , 8 ,1 ,10])
plt.subplot(2 , 3 , 2)
plt.plot(x , y)
plt.title("Marketing")
# plot3
x = np.array([0 , 1 , 2, 3])
y = np.array([3 , 8 ,1 ,10])
plt.subplot(2 , 3 , 3)
plt.plot(x , y)
plt.title("Coding")
# plot4
x = np.array([0 , 1 , 2, 3])
y = np.array([3 , 60,1 ,10])
plt.subplot(2 , 3 , 4)
plt.plot(x , y)
plt.title("Patent")
# plot5
x = np.array([0 , 1 , 2, 3])
y = np.array([3 , 8 ,1 ,10])
plt.subplot(2 , 3 , 5)
plt.plot(x , y)
plt.title("Network")
# plot6
x = np.array([0 , 1 , 2, 3])
y = np.array([3 , 8 ,1 ,80])
plt.subplot(2 , 3 , 6)
plt.plot(x , y ,linewidth = "2.5" , c = "r" , marker ='o')
plt.title("sales Executive")
plt.suptitle("Our Marketing record")
plt.show() 


#__________________BEST OF LUCK ____________________#