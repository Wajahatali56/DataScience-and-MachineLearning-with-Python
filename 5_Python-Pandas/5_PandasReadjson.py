
#JSON: Big data sets are normally stored and extracted as JSON.It is a plain text , but it has a format of an oject.

# Loading the json into a dataframe:

import pandas as pd
wajahat = pd.read_json(r'C:\Users\USER PC\DATA SCIENCE with PYTHON\5_Python-Pandas\data.js')
print(wajahat.to_string())

#Dictionary as a JSON: if your JSON code is not in a file, but in a python dictionary, then you can do all below:

import pandas as pd
data ={
    "duration":{
        "0": 60 ,
        "1": 60 ,
        "2" : 60 ,
        "3" : 45,
        "4" : 45 ,
        "5" : 60 
        } ,
    "pulse":{
     "0": 111 ,
     "1": 601 ,
      "2" : 260,
      "3" : 425,
      "4" : 145 ,
      "5" : 360 
     },
      "Maxpulse":{
     "0": 1000 ,
     "1": 2000,
      "2" : 3000,
      "3" : 4000,
      "4" : 5000 ,
      "5" : 4500 
     },
    "Calories":{
    "0":409.1,
    "1":479.0,
    "2":340.0,
    "3":282.4,
    "4":406.0,
    "5":300.5
      }
}
datanew =pd.DataFrame(data)
print(datanew)


#__________________BEST OF LUCK ____________________#