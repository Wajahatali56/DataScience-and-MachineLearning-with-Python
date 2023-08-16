
# Logistic dist -describe growth it is basically imp in regression and neural networks.
# parameters - loc(mean -0) , scale (standard deviation -1) , size

# Draw 2*2 sample of logistic with mean at 1 and std-dev 2:

from numpy import random
wajahat = random.logistic(loc=1 , scale=2 , size=(2 , 3))
print(wajahat)

# Visualization of logistic dist:


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.logistic(size=1000) , hist=False)
plt.show() 

#__________________BEST OF LUCK ____________________#