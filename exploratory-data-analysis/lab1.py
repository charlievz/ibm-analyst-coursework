#%%
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import seaborn as sns

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"
download(filename, "automobileEDA.csv")
filename="automobileEDA.csv"
df = pd.read_csv(filename, header=0)
# print(df.dtypes)
## correlation and scatterplots + boxplots
# df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr()
# sns.regplot(x='engine-size',y='price',data=df)
# plt.ylim(0,)
# df[["engine-size", "price"]].corr()
# sns.regplot(x='highway-mpg',y='price', data=df)
# sns.regplot(x="peak-rpm", y="price", data=df)
# sns.boxplot(x='body-style',y='price',data=df)
# sns.boxplot(x='engine-location',y='price', data=df)


df['engine-location'].value_counts().to_frame()
df['engine-location'].unique()

df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
grouped_test1

grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
grouped_pivot