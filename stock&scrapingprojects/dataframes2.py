#%%
import pandas as pd
csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)
df[['Length','Artist', 'Genre']]

new_index=['a','b','c','d','e','f','g','h']
df.index = new_index
df.loc['a', 'Artist']
#%%