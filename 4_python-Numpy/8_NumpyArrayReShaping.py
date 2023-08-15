
# Reshaping - means changing the shape of an array , like adding or removing the elements.

# Reshaping from 1-D to 2-D:

import numpy as np 
wajahat = np.array([1 , 2 ,3 ,4 ,5, 6 , 7, 8 , 9 ,10 , 11 , 12])
newarr =wajahat.reshape(4 , 3)
print(newarr)

# Reshaping from 1-D to 3-D:

import numpy as np 
wajahat = np.array([1 , 2 ,3 ,4 ,5, 6 , 7, 8 , 9 ,10 , 11 , 12])
newarr =wajahat.reshape(2 , 3 , 2)
print(newarr)

# Return copy or view:

import numpy as np 
wajahat = np.array([1 , 2 ,3 ,4 ,5, 6 , 7, 8])

print(wajahat.reshape(2 , 4).base)

# Unknown dimension - you are only allowed to have one unknown dimension. pass -1:

import numpy as np 
wajahat = np.array([1 , 2 ,3 ,4 ,5, 6 , 7, 8])

print(wajahat.reshape(2 , 2 , -1)) # They automatically(-1) arrange Array into 2-D formate

# Flattening the array by converting multi-dimensional array in 1-D:

import numpy as np
wajahat = np.array([[1 , 2 , 3] , [4 , 5 ,6]])
new_array =wajahat.reshape(-1) # They automatically arrange Array into 1-D formate(-1)
print(new_array)

# There are alot of functions for changing the shapes of an array in numpy , like flatten , ravel , and also rearranging the element rot90 , flip , fliplr , flipud.They all are actually comes under advanced numpy.


#__________________BEST OF LUCK ____________________#



