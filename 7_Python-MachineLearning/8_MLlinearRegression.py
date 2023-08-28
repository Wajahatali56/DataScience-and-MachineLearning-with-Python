
# Regression: The term regression is used when you try to find out the relationship between the variables , in machine Learning and in statistical modeling that relationship is used to predict the outcomes of the future events.

# Linear Regression :  it is basically uses the relationship between the data points to draw a straight line through all of them , this line can be used to predict the future.

# How does it works :
# Now we will start by drawing a scatter plot:

'''
x is the age of cars and y is the tollboth where the cars passes.

import matplotlib.pyplot as plt
x = [5 ,7 , 8 , 7 ,2 , 17 , 2 , 9 ,4, 11, 12,9 ,6]
y = [99 , 86 , 87 , 88 , 11 , 86 , 103, 87, 94 ,78, 77 , 85 , 86]
plt.scatter(x , y)
plt.show() '''

# Now we will import scipy(scientific python)and draw the line of linear regression:
'''
import matplotlib.pyplot as plt
from scipy import stats
x = [5 ,7 , 8 , 7 ,2 , 17 , 2 , 9 ,4, 11, 12,9 ,6]
y = [99 , 86 , 87 , 88 , 11 , 86 , 103, 87, 94 ,78, 77 , 85 , 86]
slope , intercept , r  , p , std_err = stats.linregress(x , y)
def myfun(x):
    return slope * x + intercept
mymodel = list(map(myfun , x))
plt.scatter(x , y)
plt.plot(x , mymodel)
plt.show()'''

''' Lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()'''

# Defining R for relationship - it is important to know how the relationship between the values of x axis and y axis, if there is no relationsgip then the linear regression cannot be used to predict anything , then this relationship is called R and also know as coefficient of co-relation.

# The R values ranges from -1 to 1 , where 0 means no relationship and 1 and -1 means 100% realted.

# Now we will know how well does the data fit in a linear regression:
'''
from scipy import stats
x = [5 ,7 , 8 , 7 ,2 , 17 , 2 , 9 ,4, 11, 12,9 ,6]
y = [99 , 86 , 87 , 88 , 11 , 86 , 103, 87, 94 ,78, 77 , 85 , 86]
slope , intercept , r , p , std_err = stats.linregress(x , y)
print(r)'''

# Predict future values: lets try to predict the speed of 10 years old cars:
'''
from scipy import stats
x = [5 ,7 , 8 , 7 ,2 , 17 , 2 , 9 ,4, 11, 12,9 ,6]
y = [99 , 86 , 87 , 88 , 11 , 86 , 103, 87, 94 ,78, 77 , 85 , 86]
slope , intercept , r , p , std_err = stats.linregress(x , y)
def myfun(x):
    return slope * x +intercept
myspeed = myfun(10)
print(myspeed) '''

# Bad fit - lets create an example : where linear regression would not be the best method for predicting the future:
'''
import matplotlib.pyplot as plt
from scipy import stats
x = [89 , 46 , 35 , 10 , 95 , 66 , 77 , 20 , 25 , 98 , 100 , 47 , 90 , 49 , 24 ]
y = [99 , 86 , 87  ,78 , 74 , 88 , 11 , 86 , 103, 87, 94 ,78, 77 , 85 , 86]
slope , intercept , r , p , std_err = stats.linregress(x , y)
def myfun(x):
    return slope * x +intercept
mybadmodel = list(map(myfun , x))
plt.scatter(x , y)
plt.plot(x , mybadmodel)
plt.show() '''

# Now we will check the relationship with R
import numpy as np
from scipy import stats
x = [89 , 46 , 35 , 10 , 95 , 66 , 77 , 20 , 25 , 98 , 100 , 47 , 90 , 49 , 24 ]
y = [99 , 86 , 87  ,78 , 74 , 88 , 11 , 86 , 103, 87, 94 ,78, 77 , 85 , 86]
slope , intercept , r , p , std_err = stats.linregress(x , y)
print(r)


#__________________BEST OF LUCK __________________#

