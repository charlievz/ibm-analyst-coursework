#%%
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')
years = list(map(str, range(1980, 2014)))
df_can.set_index('Country', inplace=True)
df_iceland = df_can.loc['Iceland', years]
# df_iceland.plot(kind='bar')
df_iceland.plot(kind='barh', color = 'red')