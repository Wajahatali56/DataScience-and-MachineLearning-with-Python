
# creating the pie chart.

# pie() function

import matplotlib.pyplot as plt
import numpy as np

x = np.array([25 , 45 ,65 ,25])
plt.pie(x)
plt.show()

# Now we will label the pie chart

import matplotlib.pyplot as plt
import numpy as np

x = np.array([25 , 45 ,65 ,25])
mylabels = ["Srilanka" , "Pakistan" , "India" , "china"]
plt.pie(x , labels= mylabels)
plt.show() 

# Startangle parameter - the default start angel is at the x -axis but you can change start angel by specifying startangle parameter.

import matplotlib.pyplot as plt
import numpy as np

x = np.array([25 , 45 ,65 ,25])
mylabels = ["Srilanka" , "Pakistan" , "India" , "china"]
plt.pie(x , labels= mylabels , startangle= 90)
plt.show() 

# How to explode the pie chart by a value

import matplotlib.pyplot as plt
import numpy as np

x = np.array([25 , 45 ,65 ,25])
mylabels = ["Srilanka" , "Pakistan" , "India" ,"china"]
myexplode = [0.2 , 0 , 0 , 0]

plt.pie(x , labels= mylabels , explode= myexplode)
plt.show() 

# The shadow parameter for creativity

import matplotlib.pyplot as plt
import numpy as np

x = np.array([25 , 45 ,65 ,25])
mylabels = ["Srilanka" , "Pakistan" , "India" ,"china"]
myexplode = [0.2 , 0 , 0 , 0]

plt.pie(x , labels= mylabels , explode= myexplode , shadow=True)
plt.show() 

# You can also change the colors of each wedge.

import matplotlib.pyplot as plt
import numpy as np

x = np.array([25 , 45 ,65 ,25])
mylabels = ["Srilanka" , "Pakistan" , "India" ,"china"]
mycolors = ["black" , "green" , "pink" , "magenta"]

plt.pie(x , labels= mylabels , colors= mycolors)
plt.show()  


# we can also add the legend - list of explanation

import matplotlib.pyplot as plt
import numpy as np

x = np.array([25 , 45 ,65 ,25])
mylabels = ["Srilanka" , "Pakistan" , "India" ,"china"]
mycolors = ["black" , "green" , "pink" , "magenta"]

plt.pie(x , labels= mylabels , colors= mycolors)
plt.legend()
plt.show() 

# we  will add legend with header

import matplotlib.pyplot as plt
import numpy as np

x = np.array([25 , 45 ,65 ,25])
mylabels = ["Srilanka" , "Pakistan" , "India" ,"china"]
mycolors = ["black" , "green" , "pink" , "magenta"]

plt.pie(x , labels= mylabels , colors= mycolors)
plt.legend(title = "Top Countries")
plt.show() 


#__________________BEST OF LUCK ____________________#
