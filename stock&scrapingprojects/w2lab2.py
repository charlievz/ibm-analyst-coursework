#%%
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')

################################################################
# Pie charts 

df_continents=df_can.groupby('Continent',axis=0).sum()
# df_continents['Total'].plot(kind='pie',figsize=(5,6),autopct='%1.1f%%',startangle=90,shadow=True)
# plt.title('Immigration to Canada by Continent 1980-2013')
# plt.axis('equal')
# plt.legend(labels=df_continents.index, loc='upper left')
# plt.show()

colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
explode_list = [0.1, 0, 0, 0, 0.1, 0.1]
df_continents['Total'].plot(kind='pie',
                            figsize=(10,6),
                            autopct='%1.1f%%',
                            startangle=90,
                            shadow=True,
                            labels=None,
                            pctdistance=1.12,
                            colors=colors_list,
                            explode=explode_list)
plt.title('Immigration to Canada by Continent 1980-2013',y=1.12,fontsize=15)
plt.axis('equal')
plt.legend(labels=df_continents.index, loc='upper left',fontsize=7)
plt.show()

df_continents['2013'].plot(kind='pie',
                            figsize=(15,6),
                            autopct='%1.1f%%',
                            startangle=90,
                            shadow=True,
                            labels=None,
                            pctdistance=1.12,
                            explode=explode_list)
plt.title('Immigration to Canada by Continent in 2013',y=1.12,fontsize=15)
plt.axis('equal')
plt.legend(labels=df_continents.index, loc='upper left',fontsize=7)
plt.show()

################################################################
# Box plots
years = list(map(str, range(1980, 2014)))
df_can.set_index('Country', inplace=True)
df_japan = df_can.loc[['Japan'], years].transpose()
df_japan.plot(kind='box',figsize=(8,6))
plt.title('Box plot of Japanese Immigrants from 1980 - 2013')
plt.ylabel('Number of Immigrants')
plt.show()

df_CI= df_can.loc[['China', 'India'], years].transpose()
df_CI.plot(kind='box', figsize=(10, 7))
plt.title('Box plots of Immigrants from China and India (1980 - 2013)')
plt.ylabel('Number of Immigrants')
plt.show()
#%%