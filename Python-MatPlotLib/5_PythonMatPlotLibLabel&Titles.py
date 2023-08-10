
# Create labels for a plot

import matplotlib.pyplot as plt
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120])
 
y =np.array([240,250,260,270,280,290,300,310,320])

plt.plot(x, y)
plt.xlabel("Grounded scale")
plt.ylabel("Average growth")
plt.show() 

# Creating title for a plot

import matplotlib.pyplot as plt
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120])
 
y =np.array([240,250,260,270,280,290,300,310,320])

plt.plot(x, y)
plt.title("Health Monitor")
plt.xlabel("Grounded scale")
plt.ylabel("Average growth")
plt.show()

# Now we will set font property for property and labels:

import matplotlib.pyplot as plt
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120])
 
y =np.array([240,250,260,270,280,290,300,310,320])

font1 = {'family':'serif' , 'color' :'blue' , 'size' : 20}
font2 = {'family':'serif' , 'color' :'green' , 'size' : 10 }

plt.plot(x, y)

plt.title("Health Monitor" ,fontdict=font1)

plt.xlabel("Grounded scale" , fontdict=font2)
plt.ylabel("Average growth" , fontdict=font2)
plt.show()

# You can also change the location of title via "loc":

import matplotlib.pyplot as plt
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120])
 
y =np.array([240,250,260,270,280,290,300,310,320])

font1 = {'family':'serif' , 'color' :'blue' , 'size' : 20}
font2 = {'family':'serif' , 'color' :'green' , 'size' : 10 }

plt.plot(x, y)

plt.title("Health Monitor" ,fontdict=font1 ,loc='left') # By default setting is center 

plt.xlabel("Grounded scale" , fontdict=font2)
plt.ylabel("Average growth" , fontdict=font2)
plt.show()


#__________________BEST OF LUCK ____________________#