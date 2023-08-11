
# Scatter - the scatter() function plots one dot for each observation.
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array ([5 , 7, 8, 9 ,8, 6 ,34 , 7, 25, 16 , 49 , 12])
y = np.array([55 , 87, 78, 69 ,68, 36 ,73 , 47, 25, 66 , 49 , 96])

plt.scatter(x,y)
plt.show() '''

# Now we will compare 2 plots on same figure
'''
import matplotlib.pyplot as plt
import numpy as np
# day1 , age and speed of 12 cars:
x = np.array ([5 , 7, 8, 9 ,8, 6 ,34 , 7, 25, 16 , 49 , 12])
y = np.array([55 , 87, 78, 69 ,68, 36 ,73 , 47, 25, 66 , 49 , 96])
plt.scatter(x,y)

# day 2 , age and speed of 12 car

x = np.array ([1 , 2 ,9 , 8 , 7 , 9 , 5 , 4 , 17 , 8 , 33 , 8])
y = np.array([98 , 87,  69 , 69 ,49, 36 ,93 , 47, 25, 87, 119 , 196])

plt.scatter(x,y)
plt.show() '''

# Now we will set own color of markers
'''
import matplotlib.pyplot as plt
import numpy as np

# day1 , age and speed of 12 cars:
x = np.array ([5 , 7, 8, 9 ,8, 6 ,34 , 7, 25, 16 , 49 , 12])
y = np.array([55 , 87, 78, 69 ,68, 36 ,73 , 47, 25, 66 , 49 , 96])
plt.scatter(x,y , color = "green")

# day 2 , age and speed of 12 car

x = np.array ([1 , 2 ,9 , 8 , 7 , 9 , 5 , 4 , 17 , 8 , 33 , 8])
y = np.array([98 , 87,  69 , 69 ,49, 36 ,93 , 47, 25, 87, 119 , 196])

plt.scatter(x,y , color = 'hotpink')
plt.show() '''

# Now you can change color of each and individual dots
'''
import matplotlib.pyplot as plt
import numpy as np
# day1 , age and speed of 12 cars:
x = np.array ([5 , 7, 8, 9 ,8, 6 ,34 , 7, 25, 16 , 49 , 12])
y = np.array([55 , 87, 78, 69 ,68, 36 ,73 , 47, 25, 66 , 49 , 96])
colors = ["red" , "green" , "blue" , "yellow" ,"pink" ,"magenta" ,"cyan" , "hotpink" , "gray","purple" , "black" , "beige"]
plt.scatter(x,y , c=colors)
plt.show()'''

# Now we will create a color array and specify a colormap in scatter plot
'''
import matplotlib.pyplot as plt
import numpy as np
# day1 , age and speed of 12 cars:
x = np.array ([5 , 7, 8, 9 ,8, 6 ,34 , 7, 25, 16 , 49 , 12])
y = np.array([55 , 87, 78, 69 ,68, 36 ,73 , 47, 25, 66 , 49 , 96])

colors = ([0 , 34 , 56 , 73, 98 , 29 , 79 , 84 , 92 , 10 , 20 , 30])
plt.scatter(x,y,c=colors , cmap="viridis")
plt.show() '''

# you can also include colorbar in plot
'''
import matplotlib.pyplot as plt
import numpy as np
# day1 , age and speed of 12 cars:
x = np.array ([5 , 7, 8, 9 ,8, 6 ,34 , 7, 25, 16 , 49 , 12])
y = np.array([55 , 87, 78, 69 ,68, 36 ,73 , 47, 25, 66 , 49 , 96])

colors = ([0 , 34 , 56 , 73, 98 , 29 , 79 , 84 , 92 , 10 , 20 , 30])
plt.scatter(x,y,c=colors , cmap="viridis")
plt.colorbar()
plt.show() '''

# You can also change the size
'''
import matplotlib.pyplot as plt
import numpy as np
# day1 , age and speed of 12 cars:
x = np.array ([5 , 7, 8, 9 ,8, 6 ,34 , 7, 25, 16 , 49 , 12])
y = np.array([55 , 87, 78, 69 ,68, 36 ,73 , 47, 25, 66 , 49 , 96])

sizes = ([0 , 34 , 56 , 73, 98 , 29 , 79 , 84 , 92 , 10 , 20 , 30])#size of marker
plt.scatter(x,y, s=sizes)
plt.colorbar()
plt.show() '''

# alpha - you can adjust the transparency of dots

'''
import matplotlib.pyplot as plt
import numpy as np
# day1 , age and speed of 12 cars:
x = np.array ([5 , 7, 8, 9 ,8, 6 ,34 , 7, 25, 16 , 49 , 12])
y = np.array([55 , 87, 78, 69 ,68, 36 ,73 , 47, 25, 66 , 49 , 96])

sizes = ([0 , 34 , 56 , 73, 98 , 29 , 79 , 84 , 92 , 10 , 20 , 30])#size of marker
plt.scatter(x,y, s=sizes , alpha= 0.5)
plt.colorbar()
plt.show() '''


# Now we will combine color , size and alpha
import matplotlib.pyplot as plt
import numpy as np
# day1 , age and speed of 12 cars:

x = np.random.randint(100 ,size=(100))
y = np.random.randint(100 ,size=(100))
colors = np.random.randint(100 , size=(100))
sizes =np.random.randint(100 , size=(100))
plt.scatter(x , y , c= colors , s=sizes , alpha=0.5 ,cmap="nipy_spectral")
plt.colorbar()
plt.show() 


#__________________BEST OF LUCK ____________________#

