
# Multinomial dist: it is a generalization of binomial dist.
# Parameter - n(number of outcomes or possibility) , pvals(list of possibilities or outcomes) , size(shape of returned array)

# Draw a sample for dice roll:
from numpy import random
wajahat = random.multinomial(n=6 , pvals=[ 1/6 , 1/6 , 1/6 , 1/6 ,1/6 , 1/6])
print(wajahat)

# Multinomial samples will not produce a single value , they will produce one value for each pvals.


#__________________BEST OF LUCK ____________________#