
# Exponential dist : it is used for describing the time till next event that is like failure or success.
# parameters - scale(inverse of rate (see lam poisson dist chapter)),size .
# here we will draw a sample for exponential dist with 2.0 scale and 2*3 size:

from numpy import random
wajahat = random.exponential(scale=2 , size=(2 , 3))
print(wajahat)
 
# Visualization of Exponential  dist :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.exponential(size=1000) , hist=False)
plt.show() 


#__________________BEST OF LUCK ____________________#