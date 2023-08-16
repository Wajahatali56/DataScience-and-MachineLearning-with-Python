
# Binomial dist - discrete dist - binary output.
# 3-Parameters _ n(number of trials) , p(probability), size(shape-returned array)

# given 10 trials for a coin which will generate 10 data points:

from numpy import random
wajahat = random.binomial(n=10 , p = 0.5 , size=10)
print(wajahat)

# Visualization of binomial dist :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n=10 , p=0.5  , size=1000 ) , hist=True, kde =False)
plt.show() 

# Difference between normal and binomial - normal(continues) and binomial(discrete)
# I used 500 data point for binomial and under 100 data points for normal dist.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50 , scale=5 , size=1000) , hist=False , label ='normal')
sns.distplot(random.binomial(n=100 , p=0.5 , size=1000) , hist=False , label ='binomial')
plt.show()

#__________________BEST OF LUCK ____________________#

