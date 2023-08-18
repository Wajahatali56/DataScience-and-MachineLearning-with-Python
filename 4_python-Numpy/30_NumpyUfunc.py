
# ufunction - stands for universal function and they are actually numpy functions that operates on the nd-array objects.
'''
ufunc also takes additional arguments like where , dtype and out.
Vectorization - converting the iterative statements into a vector based statement.

'''
# Example without ufunc , here we will use python in-built zip():

x = [1 , 2 , 3 , 4]
y = [4 , 5 , 6 , 7]
z = []
for i , j in zip(x , y):
    z.append(i + j)
print(z)

# With ufunction , we will now use add() function:
import numpy as np
x = [1 , 2 , 3 , 4]      # or   np.array([1 , 2 , 3 , 4])
y = [4 , 5 , 6 , 7]      # or   np.array([4 , 5 , 6 , 7])
z =np.add(x , y)
print(z)


#__________________BEST OF LUCK ____________________#