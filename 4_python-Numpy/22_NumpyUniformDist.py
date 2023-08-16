
# Uniform Dist -it is only made for probability(p)
# Parameters - a(lower bound- 0.0) , b(upper bound 1.0) , size 

from numpy import random
wajahat = random.uniform(size=(2 , 3))
print(wajahat)

# Visualization of Uniform dist:

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.uniform(size=1000) , hist=False)
plt.show()


#__________________BEST OF LUCK ____________________#