
# finding GCD (greatest common denominator) , also called HCF (highest common factor).

# Here we will find the HCF of the below 2 numbers:

import numpy as np
x = 4
y = 6
znew = np.gcd(x , y)
print(znew)

# Finding the gcd in an array:
# the reduce() method will use the ufunc , in this case the gcd() function on each elements and it will reduce the array by 1 dimension.
import numpy as np
x1 = np.array([24 , 40 , 36 , 24])
xnew =np.gcd.reduce(x1)
print(xnew)



#__________________BEST OF LUCK ____________________#