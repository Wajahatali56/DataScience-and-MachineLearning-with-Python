
# Iterating Array- means going through the elements one by one or step by step like (for loop).

# Iterate the elements of 1-D:
import numpy as np
wajahat =np.array([1,2,3])
for i in wajahat:
    print(i) 
print('**************************')
# Iterate the elements of 2-D:
import numpy as np
wajahat =np.array([[1 , 2 , 3],[4, 5 ,6]])
for i in wajahat:
    print(i)
print('**************************')
# Iterate on each scalar elements of 2-D:
 
import numpy as np
wajahat =np.array([[1 , 2 , 3],[4, 5 ,6]])
for i in wajahat:
   for a in i:
       print(a)
  
# Iterate the elements of 3-D:
print('**************************')
import numpy as np
wajahat =np.array([[[1 , 2 , 3],[4, 5 ,6] , [7 , 8 , 9]]])
for i in wajahat:
    for a in i:
        for b in a:
            print(b)
print('**************************')
# Iterating arrays using the nditer() function.

# Now we will Iterate on each scalar elements:
import numpy as np
wajahat = np.array([[[1, 2] , [3,4] , [5,6] , [7 , 8]]])
for i in np.nditer(wajahat):
    print(i)
print('**************************')

# Now we will Iterate with different step sizes.
import numpy as np
wajahat =np.array([[1 , 2 , 3 , 4],[4, 5 ,6 , 7]])
for i in np.nditer(wajahat[: , ::2]):
    print(i)


#__________________BEST OF LUCK ____________________#

