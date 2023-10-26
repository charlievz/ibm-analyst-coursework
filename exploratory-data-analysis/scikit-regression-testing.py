#%%
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
# import skillsnetwork
import warnings
from sklearn.linear_model import LinearRegression
warnings.filterwarnings('ignore')

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
csv = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
filename="automobileEDA.csv"
download(csv, filename)
df = pd.read_csv(filename, header=0)

lm  = LinearRegression()

X = df[['highway-mpg']]
Y = df['price']

# x helps us predict Y
lm.fit(X, Y)

slope = lm.coef_
intercept = lm.intercept_
#Y = intercept + slope*x

# multiple linear regression
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm.fit(Z, df['price'])
