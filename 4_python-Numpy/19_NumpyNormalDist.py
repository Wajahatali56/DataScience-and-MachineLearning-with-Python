
# Normal(Gaussian) Distribution - very important.
# random.normal() method - loc(mean), scale(standard deviation) , size:
# We are generating a random distribution of size (2 , 3).
from numpy import random
wajahat = random.normal(size=(2  , 3))
print(wajahat)

# Here we will generate a random normal dist of size (2,3) with mean at 1 and standard deviation of 2:

from numpy import random
wajahat = random.normal(loc=1, scale= 2 ,size=(2 , 3))
print(wajahat)

# Visualization of normal distribution:

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000) , hist=False)
plt.show()

# The curve of a normal dist is also called bell curve.


#__________________BEST OF LUCK ____________________#
