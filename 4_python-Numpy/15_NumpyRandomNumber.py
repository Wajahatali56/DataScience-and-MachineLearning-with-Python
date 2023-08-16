
# Random meaning - something that cannot be predicted logically.

# Now we will generate a random number from 0 to 100:

from numpy import random
x = random.randint(100)
print(x)
print("********************")
# You can also generate float() number via rand():

from numpy import random
x = random.rand()
print(x)
print("********************")
# You can also generate random Array -  We will generate a 1-D array containing 5 random int from 0 to 100:

from numpy import random
x = random.randint(100 , size=(5))
print(x)
print("********************")
# You can also generate random Array -  We will generate a 2-D array with 3 rows ,each row containing 5 random int from 0 to 100:

from numpy import random
x = random.randint(100 , size=(3 , 5))
print(x)
print("********************")
# You can also generate random Array -  We will generate a 1-D array containing 5 random float:

from numpy import random
x = random.rand(5)
print(x)

print("********************")
# You can also generate random Array -  We will generate a 2-D array with 3 rows , each containing 5 random float:

from numpy import random
x = random.rand(3 , 5)
print(x)

print("********************")

# You can also generate random numbers from an array using choice():

from numpy import random
x = random.choice([3 , 8 ,0 ,9 ,179 ,67])
print(x)
print("********************")

# You can also generate random numbers from 2-D array using choice():

from numpy import random
randomarr = random.choice([3 , 8 ,0 ,9 ,179 ,67] , size=(3 , 5))
print(randomarr)


#__________________BEST OF LUCK ____________________#