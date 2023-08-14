
# Difference between numpy array copy and view :
# we will make a copy, change in original array , and display both

import numpy as np
xcopy =np.array([1 , 2 , 3 , 4, 5])
newcopy =xcopy.copy()
newcopy[0] = 40
print(xcopy)
print(newcopy)

# Now we will make a view , change original ,display both:

import numpy as np
xcopy =np.array([1 , 2 , 3 , 4, 5])
newcopy = xcopy.view()
newcopy[0] = 56
print(xcopy)
print(newcopy)


#__________________BEST OF LUCK ____________________#