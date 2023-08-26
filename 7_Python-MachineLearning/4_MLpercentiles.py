
# What are percentile?

ages = [5 , 6 , 45 , 4 , 9 , 5 , 2  ,8 , 7 , 46 , 35 , 20 , 98  ,57 , 35 ,53 , 25 , 71 ,69  , 42 ,68 ]

# numpy module has a method for finding the specified percentiles:

import numpy as np
ages = [5 , 6 , 45 , 4 , 9 , 5 , 2  ,8 , 7 , 46 , 35 , 20 , 98  ,57 , 35 ,53 , 25 , 71 ,69  , 42 ,68 ]
xnew = np.percentile(ages , 75)
print(xnew)

# What is the age of 90% people younger than ?

import numpy as np
ages = [5 , 6 , 45 , 4 , 9 , 5 , 2  ,8 , 7 , 46 , 35 , 20 , 98  ,57 , 35 ,53 , 25 , 71 ,69  , 42 ,68 ]
xnew = np.percentile(ages , 90)
print(xnew)



#__________________BEST OF LUCK ____________________#