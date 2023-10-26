import numpy as np
import pandas as pd

df_can = pd.read_excel('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

# print(df_can.head()) # prints first 10(?) rows of data
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True) # drops these unneeded columns
# print(df_can.columns)
df_can.rename(columns={'OdName':'Country','AreaName':'Continent', 'RegName':'Region'}, inplace=True) # rename columns
# print(df_can.columns)
df_can['Total'] = df_can.sum(axis=1, numeric_only = True) # add a total column

print(df_can['Total'])

