#%%
import pandas as pd
x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 'Salary':[100000, 80000, 50000, 60000]}
df = pd.DataFrame(x)
# df
# df[["ID", "Salary"]]
# df['ID']

# df.loc[2, 'Department']

df2 = df
df2 = df2.set_index("Name")
# df2.loc['Jane', 'Salary']

df.iloc[0:2, 0:3]
df.loc[0:2, "Name": "Department"]
#%%