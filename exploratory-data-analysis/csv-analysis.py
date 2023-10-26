#%%
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
# import skillsnetwork
import warnings
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression
warnings.filterwarnings('ignore')

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
csv = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'
filename="kc_house_data_NaN.csv"
download(csv, filename)
df = pd.read_csv(filename)
df.drop(['id', 'Unnamed: 0'],axis=1, inplace=True)
df.describe()

mean=df['bedrooms'].mean()
df['bedrooms'].replace(np.nan,mean, inplace=True)

mean=df['bathrooms'].mean()
df['bathrooms'].replace(np.nan,mean, inplace=True)

floors_df = df['floors'].value_counts().to_frame()
floors_df.head()

sns.boxplot(df, x='waterfront', y='price')