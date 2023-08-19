
# Dataframe: it is a 2-D data structure like a 2-D array with table include rows and columns.

import pandas as pd
data = {"cal":[420 , 250 , 590] ,"dur":[150 , 980 , 360]}
newdata =pd.DataFrame(data)
print(newdata)

# Locate rows : pandas use th loc attibute to return one or more specified rows:

import pandas as pd
data = {"cal":[420 , 250 , 590] ,"dur":[150 , 980 , 360]}
newdata =pd.DataFrame(data)
print(newdata.loc[[0]]) #also apply [0] single square brackets

# Example of returning row 0 and 1:

import pandas as pd
data = {"cal":[420 , 250 , 590] ,"dur":[150 , 980 , 360]}
newdata =pd.DataFrame(data)
print(newdata.loc[[0 ,1]])

# Named index:with the index arg, you can name own index:

import pandas as pd
data = {"cal":[420 , 250 , 590] ,"dur":[150 , 980 , 360]}
newdata =pd.DataFrame(data , index=["day1" , "day2" , "day3"])
print(newdata)

# locate the named index:

import pandas as pd
data = {"cal":[420 , 250 , 590] ,"dur":[150 , 980 , 360]}
newdata =pd.DataFrame(data , index=["day1" , "day2" , "day3"])
print(newdata.loc["day3"])

#Output in a dataframe:

import pandas as pd
data = {"cal":[420 , 250 , 590] ,"dur":[150 , 980 , 360]}
newdata =pd.DataFrame(data , index=["day1" , "day2" , "day3"])
print(newdata.loc[["day1" , "day2"]])


'''

# load the data from csv file into dataframe i.e data.csv:

import pandas as pd
fileload = pd.read_csv('data.csv')
print(fileload)  


'''


#__________________BEST OF LUCK ____________________#