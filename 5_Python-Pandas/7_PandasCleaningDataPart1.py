
#Data in a wrong format: to fix this problem , there are 2 ways: removing the rows or convert all the cells in the same format.
# Loading and reading the original dataframe:

import pandas as pd
wajahat = pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\dirtydata.csv')
print(wajahat.to_string())

# now let's try to convert all the cells in the date column into dates.via to_datetime():

import pandas as pd 
x = pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\dirtydata.csv')
x["Date"] = pd.to_datetime(x["Date"])
print(x.to_string())

# Here we will remove the rows with a NULL value in a 'Date' column.

#import pandas as pd
#x = pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with #PYTHON\5_Python-Pandas\dirtydata.csv')
#x["Date"] = pd.to_datetime(x["Date"])
#x.dropna(subset=['Date'] , inplace=True)
#print(x.to_string())



#__________________BEST OF LUCK ____________________#