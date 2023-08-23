
# Optimizers in Scipy : they are set of procedures define in scipy that either find the minimum value of a function or a root of an equation.
# optimization dunction: all the algorithms which helps in minimizing the data.
#Root of an equation: x + cos(x) , we will solve it via optimize.root function:
# This function takes 2 arguments : "fun" & x ^ 0:

# Example : here we will find the root of the equation x + cos(x):

from scipy.optimize import root
from math import cos 

def eqn(x):
    return x + cos(x)
myroot = root(eqn , 0)
print(myroot.x)

# Here we want the info about not just x but the whole root:


from scipy.optimize import root
from math import cos 

def eqn(x):
    return x + cos(x)
myroot = root(eqn , 0)
print(myroot)
#Minimizing the function or data - high point are maxima and low points are minma

# Find the Minimum:
# We use scipy.optimize.minimize().it uses 3 arguments : "fun" , x^0 and method: it also has some legal values : "CG" ,"BFGS" , "NEWTON-CG", "L-BFGS-B","TNC" , "COBYLA" ,"SLSQP".

# callback: function called after each iteration of optimizations.

# Example of the above - in which we will minimize the function:x^2 + x +2 with BFGS:

from scipy.optimize import minimize
def eqn(x):
    return x**2 + x + 2
mymin= minimize(eqn , 0 , method='BFGS')
print(mymin)




#__________________BEST OF LUCK ____________________#
