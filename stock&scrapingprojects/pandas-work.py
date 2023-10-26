#%%
import pandas as pd
import numpy as np
import requests

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)

path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
download(path, 'auto.csv')
df = pd.read_csv('auto.csv')
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers
df.replace('?', np.NaN, inplace=True)
missing_data = df.isnull()
missing_data.head()

for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")

avg_normalized_loss = df['normalized-losses'].astype('float').mean(axis=0)
print('avg of normalized losses', avg_normalized_loss)
df['normalized-losses'].replace(np.NaN,avg_normalized_loss,inplace=True)

avg_bore=df['bore'].astype('float').mean(axis=0)
print("Average of bore:", avg_bore)
df["bore"].replace(np.NaN, avg_bore, inplace=True)

avg_stroke=df['stroke'].astype('float').mean(axis=0)
print("Average of bore:", avg_stroke)
df["stroke"].replace(np.NaN, avg_stroke, inplace=True)