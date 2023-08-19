
# Removing the duplicate values : first you need to discover the duplicate values via duplicated() method.

#loading and reading the original dataframe:

import pandas as pd
wajahat = pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\dirtydata.csv')
print(wajahat.to_string())

# returns True for every row that is duplicate otherwise return false:

import pandas as pd
wajahat = pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\dirtydata.csv')
print(wajahat.duplicated())

# Removing the duplicate from the data set via drop_duplicates():

import pandas as pd
wajahat = pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\dirtydata.csv')
wajahat.drop_duplicates(inplace=True)
print(wajahat.to_string())



#__________________BEST OF LUCK ____________________#
