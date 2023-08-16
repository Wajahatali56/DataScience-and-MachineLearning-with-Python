
# Matplotlib(Pyplot) - seaborn _ it is a libraray that use matplotlib underneath to plot graph i.e pyplot.
# Distplot - distribution plot(curve plot -histogram)
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0 , 1 , 2 , 3 , 4 ,5])
plt.show()

# Plotting a distplot without the histogram:
import matplotlib.pyplot as plt
import seaborn as sns
x = [0 , 1 , 2 , 3 , 4 ,5]
sns.distplot(x , hist=False)  # Another way to define array : sns.distplot([0 , 1 , 2 , 3 , 4 ,5] ,hist=False)
plt.show()

#__________________BEST OF LUCK ____________________#


