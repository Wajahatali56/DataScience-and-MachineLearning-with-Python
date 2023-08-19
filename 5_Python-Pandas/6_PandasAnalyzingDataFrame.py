
# Viewing the data: one of the most used method for a quick overview of the dataframe is the head() method.This method returns the headers and a specified number of rows:

# here we will print the 1st 10 rows in the dataFrame:

import pandas as pd
wajahat =pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\data.csv')
print(wajahat.head(10)) 

# Here we will print the last 10 rows in the dataframe:


import pandas as pd
wajahat =pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\data.csv')
print(wajahat.tail(10)) 

# What if you want the information about the data in the dataframe: via info()
import pandas as pd
df =pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\data.csv')
print(df.info())

# This is another example dataset

import pandas as pd
df =pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\datafile.csv')
print(df.info())



#__________________BEST OF LUCK ____________________#