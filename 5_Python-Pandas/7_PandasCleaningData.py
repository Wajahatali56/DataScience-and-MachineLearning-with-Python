# cleaning data : it means fixing the bad data in your data set. Bad data could be empty cell , data in a wrong format , duplicate data and wrong data:

# Empty cell: it will give you wrong result always , we will have to remove the rows always that contains the bad data.

# Loading and reading the original dataframe:

import pandas as pd
wajahat = pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\dirtydata.csv')
print(wajahat.to_string())

#here we will return a new data frame with no empty cell:

import pandas as pd
wajahat = pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\dirtydata.csv')
wajahatnew =wajahat.dropna()
print(wajahatnew.to_string())

# If at any cases you wants to change the original dataframe, than use the inplace=True argument.it will remove the rows containing the NUL(NaN) values.


import pandas as pd
wajahat = pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\dirtydata.csv')
wajahat.dropna(inplace=True)
print(wajahat.to_string())

# Replacing the empty value:we will use fillna() method which will allow us to replace the empty cell with a value.

import pandas as pd
wajahat = pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\dirtydata.csv')
wajahat.fillna(56 ,inplace=True)
print(wajahat.to_string())

# To replace only the empty value for one column , you need to specify the column name:

import pandas as pd
wajahat = pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\dirtydata.csv')
wajahat["Date"].fillna(56 ,inplace=True)
print(wajahat.to_string())


# here we can also replace the empty cell using mean() , median() or mode().
# Calculate the MEAN and replace the empty values with it:

import pandas as pd
wajahat = pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\dirtydata.csv')
x = wajahat["Calories"].mean()
wajahat["Calories"].fillna(x , inplace=True)
print(wajahat.to_string())


# Calculate the MEDIAN and replace the empty values with it:

import pandas as pd
wajahat = pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\dirtydata.csv')
x = wajahat["Calories"].median()
wajahat["Calories"].fillna(x , inplace=True)
print(wajahat.to_string())

# Calculate the MODE and replace the empty values with it:

import pandas as pd
wajahat = pd.read_csv(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\dirtydata.csv')
x = wajahat["Calories"].mode()[0]
wajahat["Calories"].fillna(x , inplace=True)
print(wajahat.to_string())




#__________________BEST OF LUCK ____________________#