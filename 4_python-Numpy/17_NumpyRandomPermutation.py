
# Permutation refers to an arrangement of elements like [3 , 2 , 1] is permutation of [1 , 2 ,3] and vice versa.

# the numpy random module provides two methods: shuffle() and permutation()

# Now we will randomly shuggle elements for the below array:

from numpy import random
import numpy as np

wajahat = np.array([1 , 2 ,3 ,4 ,5])
random.shuffle(wajahat)
print(wajahat)
print("********************")
# Now we will generate a permutation of elements for the below array:
# The permutation() method leaves the original array unchanged.
from numpy import random
import numpy as np

wajahat = np.array([1 , 2 ,3 ,4 ,5])
print(random.permutation(wajahat))


#__________________BEST OF LUCK ____________________#