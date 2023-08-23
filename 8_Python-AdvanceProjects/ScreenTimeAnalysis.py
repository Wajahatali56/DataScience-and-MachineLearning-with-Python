
# Screen Time Analysis is the task of analyzing and creating a report on which applications and websites are used by the user for how much time.Apple devices have one of the best ways of creating a screen time report.

import pandas as pd
import numpy as np
import plotly.express as px
import statsmodels.api as sm 
import plotly.graph_objects as go

data = pd.read_csv(r"C:\Users\USER PC\DATA SCIENCE with PYTHON\8_Python-AdvanceProjects\Screentime.csv")

print(data.head())
print(data.isnull().sum())
print(data.describe())

figure = px.bar(data_frame=data , x="Date" , y="Usage" , color="App" , title="Usage Graph by Wajahat ali")
figure.show()

figure = px.bar(data_frame=data , x="Date" , y="Notifications" , color="App" , title="Notification Graph by Wajahat ali")
figure.show()

figure = px.bar(data_frame=data , x="Date" , y="Times opened" , color="App" , title="Time opened Graph by Wajahat ali")
figure.show()

figure = px.scatter(data_frame=data , x="Notifications" , y="Usage" ,size="Notifications" , trendline="ols" , title="Relationship between Number of Notification and amount of usage")
figure.show()