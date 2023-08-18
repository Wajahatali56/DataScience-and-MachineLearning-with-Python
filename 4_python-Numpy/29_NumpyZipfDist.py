
# Zipf dist - its defination is like .. commom word in english has occurs bearly 1/5 times as of the most urdu words.
# parameters - a (dist param) , size 
# Sample for zipf dist with a as 2 with size 2 * 3:

from numpy import random
randarr = random.zipf(a=2 , size=(2 , 3))
print(randarr)

# Visulization of zipf dist:

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 
wajahat =random.zipf(a=2 , size=1000)
sns.distplot(wajahat [wajahat < 10], kde= False)
plt.show()


#__________________BEST OF LUCK ____________________#