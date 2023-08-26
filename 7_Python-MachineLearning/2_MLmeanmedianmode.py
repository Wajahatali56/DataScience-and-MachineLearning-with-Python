
# Data set :[99 , 86 , 87 , 88 , 111 , 86 , 103 , 87 , 83 , 85 , 96 , 92 , 75]
# In ML and in maths also there are basically three values that are actually interest to us:
# Mean : the avg value
# median:the mid point value
# mode:the most common value

# Here in this example we have speed of 13 cars:

#speed = [99 , 86 , 87 , 88 , 111 , 86 , 103 , 87 , 83 , 85 , 96 , 92 , 75]
# Mean : to calculate the mean , sum of all values 
# Sum of all cars/speed(99 + 86 + 87 + 88 + 111 + 86 + 103 + 87 + 83 + 85 + 96 + 92 + 75)/13
import numpy as np
speed = [99 , 86 , 87 , 88 , 111 , 86 , 103 , 87 , 83 , 85 , 96 , 92 , 75]
x =np.mean(speed)
print(x) # 90.62 is its avg value

# Median : here we will find the middle value:
import numpy as np
speed = [99 , 86 , 87 , 88 , 111 , 86 , 103 , 87 , 83 , 85 , 96 , 92 , 75]
x =np.median(speed)
print(x)

# speed = [2  , 4, 6 , 8, 10 ,12] , 6+8/2=7

# Mode: the value that appears most numbers of times:

from scipy import stats
speed = [99 , 86 , 81 , 88 , 111 , 86 , 103 , 87 , 83 , 86 , 96 , 86 , 75]
xnew = stats.mode(speed)
print(xnew)


#__________________BEST OF LUCK ____________________#