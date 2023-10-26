#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl

mpl.style.use('ggplot')

df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')
df_can.set_index('Country', inplace=True)
print('data dimensions', df_can.shape)
years = list(map(str, range(1980, 2014)))
df_can.sort_values(['Total'], ascending=False, axis = 0, inplace=True)
df_top5 = df_can.head()
df_top5 = df_top5[years].transpose()
df_top5.head()
df_top5.index = df_top5.index.map(int)
# using scripting layer
df_top5.plot(kind='area', stacked=False,figsize=(20,10))
plt.title('Immigration Trend of Top 5 Countries')
plt.show()

# using artist layer
ax = df_top5.plot(kind='area', alpha=0.25, figsize=(20,10))
ax.set_title('Immigration Trend of Top 5 Countries')
ax.set_ylabel('# of Immigrants')
ax.set_xlabel('Years')
#%%