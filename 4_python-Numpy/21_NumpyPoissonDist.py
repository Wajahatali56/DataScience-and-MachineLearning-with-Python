
# Poisson Dist - it estimates how many times an event an happen.
# parameters - lam(number of occurance or rate) , size
# Generate 1 * 10 dist for the occurance 2:
from numpy import random
wajahat = random.poisson(lam=2 , size=10)
print(wajahat)

# Visualization of poisson dist:

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.poisson(lam=2 , size=1000 ) , kde =False)
plt.show() 

# Presenting both the plots in same figure normal and poisson dist.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(loc=50 , scale=7, size=1000 ) , hist=False , label='Normal')
sns.distplot(random.poisson(lam=50 , size=1000) , hist=False , label='poisson')
plt.show()

# n*p == lam 
 

#__________________BEST OF LUCK ____________________#
