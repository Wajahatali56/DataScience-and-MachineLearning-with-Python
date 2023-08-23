
# For the iphone sales analysis task , I have colected a dataset containing data about sales of iphones on Flipkart.It will be an ideal dataset to analyze the sales of iphone

import pandas as pd
import numpy as np
import plotly.express as px 
import statsmodels.api as sm
import plotly.graph_objects as go

data = pd.read_csv(r"C:\Users\USER PC\DATA SCIENCE with PYTHON\8_Python-AdvanceProjects\apple_products.csv")

# print(data.head())
#print(data.describe())
#print(data.isnull().sum())

highrated = data.sort_values(by=["Star Rating"] , ascending=False)
highrated = highrated.head(10)


# print(highrated['Product Name'])
iphone = highrated['Product Name'].value_counts()
label = iphone.index
counts = highrated["Number Of Ratings"]
figure = px.bar(highrated , x=label , y= counts , title="Number of ratings of highest rated Iphone")
figure.show()


iphone = highrated['Product Name'].value_counts()
label = iphone.index
counts = highrated["Number Of Reviews"]
figure = px.bar(highrated , x=label , y= counts , title="Number of Reviews of highest rated Iphone")
figure.show()

figure = px.scatter(data_frame= data , x="Number Of Ratings" , y="Sale Price" , size="Discount Percentage" , trendline="ols" , title="Relationship between sale price and number of reviews of iphones" , trendline_scope='overall')
figure.show()

figure = px.scatter(data_frame= data , x="Number Of Ratings" , y="Discount Percentage" , size="Sale Price" , trendline="ols" , title="Relationship between sale price and number of reviews of iphones" , trendline_scope='overall')
figure.show()