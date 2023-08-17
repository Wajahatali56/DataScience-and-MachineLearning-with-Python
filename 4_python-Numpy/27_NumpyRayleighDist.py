
# Rayleigh Dist - it is used in signal processing .
#parameters -scale (standard deviation , how flat the distribution is  ... default 1.0) , size.
#Sample for Rl with scale of 2.0 with size of 2*3 :

from numpy import random
randarr = random.rayleigh(scale=2 , size=(2 , 3))
print(randarr)

# Visualization of rayleigh dist :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 
sns.distplot(random.rayleigh(size=1000) , hist=False)
plt.show()


#__________________BEST OF LUCK ____________________#