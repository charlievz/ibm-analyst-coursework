#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl

# print('Matplotlib version: ', mpl.__version__)
mpl.style.use(['classic'])

years = list(map(str, range(1980, 2014)))
df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')
df_can.set_index('Country', inplace=True)

haiti = df_can.loc['Haiti', years]
haiti.plot()
plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.text(20, 6000, '2010 Earthquake')
plt.show()

df_CI = df_can.loc[['India', 'China'], years]
df_CI = df_CI.transpose()
df_CI.plot()

plt.title('Immigration from India and China')
plt.ylabel('Num of Immigrants')
plt.xlabel('Years')
plt.show()

df_can['Total'] = df_can.sum(axis=1, numeric_only = True)
df_can.head()
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
df_top5 = df_can.head(5)
df_top5 = df_top5[years].transpose() 
df_top5.plot(kind='line', figsize=(14, 8))
plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()
# %%
