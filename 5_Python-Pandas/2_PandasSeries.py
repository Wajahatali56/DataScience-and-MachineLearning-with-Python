
# A pandas series is like a column in a table , it is 1-D array which holds data of any type.
#here we will create a simple pandas series:

import pandas as pd
list1 = [1 , 7 , 5]
listnew =pd.Series(list1)
print(listnew)

# Labeling - label can be use to access a specified value.

import pandas as pd
list1 = [1 , 7 , 5]
listnew =pd.Series(list1)
print(listnew[0])

# with create label you can create your own name labels:

import pandas as pd
list1 = [1 , 7 , 5]
listnew =pd.Series(list1 , index=["x" , "y" , "z"])
print(listnew)

# Labeling - label can be use to access a specified value.(after creating own label):

import pandas as pd
list1 = [1 , 7 , 5]
listnew =pd.Series(list1 , index=["x" , "y" , "z"])
print(listnew[["z" , "x"]])

# You can also use a key or value object like a dictionary , when creating a series.
#here we will create a simple pandas series from a dictionary.

import pandas as pd
cal = {"day1" : 340 ,"day2":290 , "day3":700}
calnew =pd.Series(cal)
print(calnew)

# now we will create a series using only data from day1 and day2:

import pandas as pd
cal = {"day1" : 340 ,"day2":290 , "day3":700}
calnew =pd.Series(cal , index=["day1" , "day2"])
print(calnew)

# DataFrame: Data sets in pandas are usually multidimensional tables , and they are called DataFrames.
#Series are like columns and dataframes is the whole table.

# we will create a dataframe from 2 series:

import pandas as pd
dict1 = {"cal" :[400 , 500 , 600] , "dur":[10 , 20 , 40]}
dictnew = pd.DataFrame(dict1)
print(dictnew)


#__________________BEST OF LUCK ____________________#