
# Pareto dist - 80 : 20 (20% factors cause 80% outcome or results).
# Parameters - a(shape param) , size.
# Sample for pareto with shape 2 with size 2*3:

from numpy import random
randarr = random.pareto(a=2 , size=(2 , 3))
print(randarr)

# Visualization of rayleigh dist :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 
sns.distplot(random.pareto(a=2 ,size=1000) , kde=False)
plt.show()


#__________________BEST OF LUCK ____________________#

