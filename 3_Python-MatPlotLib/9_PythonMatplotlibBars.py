# Vertical Bars - bar()

import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3 , 8 , 1 ,10])
plt.bar(x , y)
plt.show()

# Horizontal Bars - barh()
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3 , 8 , 1 ,10])
plt.barh(x , y)
plt.show() 

# change Color of bar() and barh()

import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3 , 8 , 1 ,10])
plt.bar(x , y , color ="green")
plt.show() 

# change the bar width

import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3 , 8 , 1 ,10])
plt.bar(x , y , width= 0.5)
plt.show()

# For horizontal bar you have to use height instead of width

import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3 , 8 , 1 ,10])
plt.barh(x , y , height= 0.5) #barh represent horizontal bar
plt.show()


#__________________BEST OF LUCK ____________________#