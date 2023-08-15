
# Searching array - you can search an array for a certain value and return the indexs that get the match by using where().

import numpy as np
wajahat = np.array([1 , 2, 3 ,4 ,5 , 4 , 4])
newindex = np.where(wajahat == 4)
print(newindex)

# Now we will find the indexes where the values are even:

import numpy as np
wajahat = np.array([1 , 2, 3 ,4 ,5 , 6 , 7 , 8])
newindex = np.where(wajahat %2 == 0)
print(newindex)

# Now we will find the indexes where the values are odd:

import numpy as np
wajahat = np.array([1 , 2, 3 ,4 ,5 , 6 , 7 , 8])
newindex = np.where(wajahat %2 == 1) #(!=)
print(newindex)

# Searchsorted() - perform binary search in array.

# We will find the index where the value 7 should be inserted:
import numpy as np
x = np.array([1 , 2, 3, 4 , 5 , 6])
newx =np.searchsorted(x , 5)
print(newx) 

# Now we will search from right side:
import numpy as np
wajahat = np.array([1 , 2, 3, 4 , 5 , 6])
newx =np.searchsorted(wajahat ,  6 , side='right')# by default it search from left 
print(newx)

# How to search multiple values:

import numpy as np
x = np.array([1 , 3, 4 , 10])
newx =np.searchsorted(x , [ 2 , 5 , 15])
print(newx)


#__________________BEST OF LUCK ____________________#