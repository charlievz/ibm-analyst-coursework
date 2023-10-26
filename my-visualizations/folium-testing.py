#%%
import folium
import pandas as pd
import numpy as np

canada_map = folium.Map(location=[56.1304, -106.3468], zoom_start=4)
# folium.Marker(location=[51.2538,-85.3232], popup='Ontario').add_to(canada_map)

ontario = folium.FeatureGroup()
ontario.add_child(folium.CircleMarker([52.25,-85.32], radius=5,color='red', fill_color='red'))
canada_map.add_child(ontario)
# canada_map

world_map = folium.Map(location=[56.130, -106.35],zoom_start=4, tiles='Stamen Terrain')
# world_map

df_incidents = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Police_Department_Incidents_-_Previous_Year__2016_.csv')
limit = 100
df_incidents = df_incidents.iloc[0:limit, :]
latitude = 37.77
longitude = -122.42
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# loop through the 100 crimes and add each to the map
for lat, lng, label in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.CircleMarker(
        [lat, lng],
        radius=5, # define how big you want the circle markers to be
        color='yellow',
        fill=True,
        popup=label,
        fill_color='blue',
        fill_opacity=0.6
    ).add_to(sanfran_map)
sanfran_map
# %%
