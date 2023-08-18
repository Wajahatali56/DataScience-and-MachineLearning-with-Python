
# Rounding decimals : there are 5 ways of rounding off the decimals innumpy : truncation , fix , rounding, floor , ceil.

#trunction : trunc() and fix() -here we are truncating the below array , these command remove the decimals and returns the float number closest to zero:

import numpy as np
x1 = np.trunc([-3.111 , 3.667])
print(x1)

# Example of fix():

import numpy as np
x1 = np.fix([-3.111 , 3.667])
print(x1)

# rounding: the around() function increments preceding digit or decimal by nearest to 1: if n>5 =1 or n<5 =0:

import numpy as np
x1 = np.around(3.7881 , 2)
print(x1)

#floor() - round off decimals to the lower integers:

import numpy as np
x1 = np.floor([-3.111 , 3.667])
print(x1)

#ceil() - round off decimals to the upper integers:

import numpy as np
x1 = np.ceil([-3.111 , 3.667])
print(x1)


#__________________BEST OF LUCK ____________________#