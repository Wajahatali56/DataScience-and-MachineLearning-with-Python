
#Arithmetic operators : + , - , / ,* 
# By using ufunc additional arguments like where , dtype and out.

# Here we will use add():
print("****** Addition********")
import numpy as np
x1 = np.array([10 , 11 , 12 , 13 , 14 , 15])
x2 =np.array([20 , 21 , 22 , 23 , 24 , 25])
xnew =np.add(x1 , x2)
print(xnew)

# Example of subtracting the values:
print("****** Subtraction********")

import numpy as np
x1 = np.array([10 , 11 , 12 , 13 , 14 , 15])
x2 =np.array([20 , 21 , 22 , 23 , 24 , 28])
xnew =np.subtract(x1 , x2)
print(xnew)

# Example of multiplication :
print("****** Multiplication********")

import numpy as np
x1 = np.array([10 , 11 , 12 , 13 , 14 , 15])
x2 =np.array([20 , 21 , 22 , 23 , 24 , 28])
xnew =np.multiply(x1 , x2)
print(xnew)

# Example of division :
print("****** Division********")

import numpy as np
x1 = np.array([10 , 11 , 12 , 13 , 14 , 15])
x2 =np.array([20 , 21 , 22 , 23 , 24 , 28])
xnew =np.divide(x1 , x2)
print(xnew)

# Power() function raises the value from the 1st array to the power of the values of the 2nd array and return the results in a new array.
print("****** Power********")

import numpy as np
x1 = np.array([10 , 11 , 12 , 13 , 14 , 15])
x2 =np.array([2 , 4 , 3 , 4 , 8 ,10])
xnew =np.power(x1 , x2)
print(xnew)

# Remainder - mod() and remainder() functions returns the remainder of the 1st array corresponding to the 2nd array , and result in the new array.

print("****** Remainder********")

import numpy as np
x1 = np.array([10 , 11 , 12 , 13 , 14 , 15])
x2 =np.array([3 , 4 , 3 , 4 , 8 ,10])
xnew =np.mod(x1 , x2)
print(xnew)

#by using remainder():

print("****** Remainder-1********")

import numpy as np
x1 = np.array([10 , 11 , 12 , 13 , 14 , 15])
x2 =np.array([3 , 4 , 3 , 4 , 8 ,10])
xnew =np.remainder(x1 , x2)
print(xnew)

# quotient and mod (remainder) - the divmod() function returns both the quotient and mod:

print("****** Quotient&Remainder********")

import numpy as np
x1 = np.array([10 , 11 , 12 , 13 , 14 , 15])
x2 =np.array([3 , 4 , 3 , 4 , 8 ,10])
xnew =np.divmod(x1 , x2)
print(xnew)

# absolute() and abs() - do the same operation but here we should use absolute() to avoide confusion with python in built function math.abs():
print("****** absolutevalues********")

import numpy as np
x1 = np.array([-2 , -99 , -987 , -64])
xnew = np.absolute(x1)
print(xnew)


#__________________BEST OF LUCK ____________________#