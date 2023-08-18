
# To create your own ufunction , you have to define a function , like you do in normal function in python , then you add it to the numpy function with frompyfunc() method.
# Arguments of frompyfunc(): function , inputs , outputs.

#Create your own ufunction for addition:

import numpy as np
def myadd(x,y):
    return x + y

myad = np.frompyfunc(myadd , 2 , 1)
print(myadd([1 , 2 , 3 , 4] , [5 , 6  , 7 , 8 ]))

# Checking type if this function is ufunc or not:
import numpy as np
print(type(np.add))

# concatenate()
import numpy as np
print(type(np.concatenate))

'''
what if ufunc does not exist - please comment it while running the code ?

import numpy as np
print(type(np.yuory))
'''

# use an if statement to check if the function is a ufunc or not:
import numpy as np
if type(np.add) == np.ufunc:
    print('yes , this is ufunc')
else:
    print('this is not a ufunc')


#__________________BEST OF LUCK ____________________#
