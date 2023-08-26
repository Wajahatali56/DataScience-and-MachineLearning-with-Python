
# Standard Deviation:
speed = [86 , 87 , 88 ,86 ,87 ,85 ,86]

# There are two types of SD: low SD snd high SD.

# Example : for low SD
import numpy as np
speed = [86 , 87 , 88 ,86 ,87 ,85 ,86]
newspeed = np.std(speed)
print(newspeed)


# Ex : for high SD:


import numpy as np
xspeed = [32 ,111, 138 ,28 ,59 ,77 ,97]
yspeed = np.std(xspeed)
print(yspeed)

# Variance : how the values are spread.
# if you take the squre root of the variance you will get the SD.

# to calculate the variance you have to do the below thing:
#(32 + 111+ 138 +28 +59 +77 +97)/7 = 77.42
'''
32 - 77.4 = -45.6  -> square root = 2079.16
111 - 77.4 = -45.6  -> square root = 1122.25
138- 77.4 = -45.6  -> square root = 3794.56
28 - 77.4 = -45.6  -> square root =2440.36
59 - 77.4 = -45.6  -> square root = 338.56
77- 77.4 = -45.6  -> square root = 0.25
97 - 77.4 = -45.6  -> square root = 384.16

The variance is the avg number of these squared difference:

(2079.16 +1122.25+3794.56+2440.36+338.56+ 0.25+384.16)/7 = 1451.05

AS we learned the formula to find SD is the square root of the variance.
Square of 1451.05 = 37.84

'''
# Example of std()
import numpy as np
xspeed = [32 ,111, 138 ,28 ,59 ,77 ,97]
yspeed = np.std(xspeed)
print(yspeed)

# symbol of SD and Variance
# SD = σ , V = σ2


#__________________BEST OF LUCK ____________________#