
# Adding grid lines to a plot via "grid()"

'''
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120])
 
y =np.array([240,250,260,270,280,290,300,310,320])

font1 = {'family':'serif' , 'color' :'blue' , 'size' : 20}
font2 = {'family':'serif' , 'color' :'green' , 'size' : 10 }


plt.title("Health Monitor" ,fontdict=font1)

plt.xlabel("Grounded scale" , fontdict=font2)
plt.ylabel("Average growth" , fontdict=font2)

plt.plot(x, y)
plt.grid()

plt.show()'''


# Now we will specify which grid lines to displays via x-axis or y-axis
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120])
 
y =np.array([240,250,260,270,280,290,300,310,320])

font1 = {'family':'serif' , 'color' :'blue' , 'size' : 20}
font2 = {'family':'serif' , 'color' :'green' , 'size' : 10 }


plt.title("Health Monitor" ,fontdict=font1)

plt.xlabel("Grounded scale" , fontdict=font2)
plt.ylabel("Average growth" , fontdict=font2)

plt.plot(x, y)
plt.grid(axis='x')

plt.show()'''

# Setting up the line properties from grid

import matplotlib.pyplot as plt
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120])
 
y =np.array([240,250,260,270,280,290,300,310,320])

font1 = {'family':'serif' , 'color' :'blue' , 'size' : 20}
font2 = {'family':'serif' , 'color' :'green' , 'size' : 10 }


plt.title("Health Monitor" ,fontdict=font1)

plt.xlabel("Grounded scale" , fontdict=font2)
plt.ylabel("Average growth" , fontdict=font2)

plt.plot(x, y)
plt.grid(color = 'green' , linestyle ="--" , linewidth = 1.5)
plt.show()


#__________________BEST OF LUCK ____________________#