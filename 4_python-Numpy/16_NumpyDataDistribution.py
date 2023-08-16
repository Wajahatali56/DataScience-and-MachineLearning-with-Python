
# Data distribution is a list of all possible value and how often each value occur - Such lists are important when working with statistics and data science.

# Random Distribution - probability function.
# Now we will generate 1-D array with 100 values where each value has to be (3 , 5 , 7 , 9):

# The probability for the value 3 is set to be 0.1
# The probability for the value 5 is set to be 0.3
# The probability for the value 7 is set to be 0.6
# The probability for the value 9 is set to be 0
# Sum of all probability numbers should be '1'.

from numpy import random
wajahat = random.choice([3 , 5 , 7 , 9] , p=[0.1 , 0.3 , 0.6 , 0.0] ,size=(100)) 
print(wajahat)
print("********************")
# Now will return 2-D with 3 rows , each containing 5 values:

from numpy import random
wajahat = random.choice([3 , 5 , 7 , 9] , p=[0.1 , 0.3 , 0.6 , 0.0] ,size=(3 , 5)) 
print(wajahat)


#__________________BEST OF LUCK ____________________#