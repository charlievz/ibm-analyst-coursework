#%%
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')

# df_can['2013'].plot(kind='hist')
# plt.title('histogram of immigration from 196 countries in 2013')
# plt.ylabel('Num of countries')
# plt.xlabel('Number of immigrants')
# plt.show()

count, bin_edges = np.histogram(df_can['2013'])
df_can['2013'].plot(kind='hist', xticks = bin_edges)
plt.title('histogram of immigration from 196 countries in 2013')
plt.ylabel('Num of countries')
plt.xlabel('Number of immigrants')
plt.show()