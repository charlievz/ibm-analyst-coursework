# Import required libraries
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

age_array = np.random.randint(20,50,60)
income_array = np.random.randint(10000,300000,100)

fig = go.Figure()
fig.add_trace(go.Scatter(x=age_array, y=income_array,mode='markers',marker=dict(color='blue')))
# fig.show()


numberofbicyclessold_array=[50,100,40,150,160,70,60,45]
# Define an array containing months
months_array=["Jan","Feb","Mar","April","May","June","July","August"]

fig = go.Figure()
fig.add_trace(go.Scatter(x=months_array,y=numberofbicyclessold_array,mode='lines',marker=dict(color='green')))
# fig.show()
fig.update_layout(title='Bicycle sales',xaxis_title='Months',yaxis_title='Number of Bicycles sold')
# fig.show()

#using plotly express
heights_array = np.random.normal(160, 11, 200)
fig=px.histogram(x=heights_array,title='Distribution of Heights')
# fig.show()

exp_percent= [20, 50, 10,8,12]
house_holdcategories = ['Grocery', 'Rent', 'School Fees','Transport','Savings']
fig = px.pie(values=exp_percent,names=house_holdcategories,title='household expenditure')
fig.show()