#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.style.use('ggplot')

df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')
years = list(map(str, range(1980, 2014)))
df_can.set_index('Country', inplace=True)
df_japan = df_can.loc[['Japan'], years].transpose()
df_japan.plot(kind='box')
plt.title('Box plot of Japanese immigrants to Canada from 1980-2013')
plt.ylabel('Number of immigrants')
plt.show()
#%%