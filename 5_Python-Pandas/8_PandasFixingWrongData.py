
# Wrong data: its only a wrong data
#loading and reading the original dataframe:

import pandas as pd
wajahat = pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\dirtydata.csv')
print(wajahat.to_string())

# Here we will set "Duration" = 45 in row 7:
import pandas as pd
wajahat = pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\dirtydata.csv')
wajahat.loc[7 , 'Duration'] = 45
print(wajahat.to_string())

# for larger data set: now here we will loop through all the values in "Duration" column, if value is higher than 120 than set it to 120.

import pandas as pd
wajahat = pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\dirtydata.csv')
for i in wajahat.index:
    if wajahat.loc[i , "Duration" ] > 120:
        wajahat.loc[i , "Duration"] = 120
print(wajahat.to_string())

#  You can also remove the rows for wrong data in larger datasets:

import pandas as pd
wajahat = pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\dirtydata.csv')
for i in wajahat.index:
    if wajahat.loc[i , "Duration" ] > 120:
        wajahat.drop(i ,inplace=True) 
print(wajahat.to_string())



#__________________BEST OF LUCK ____________________#
