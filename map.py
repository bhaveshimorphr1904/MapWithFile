from typing import List
import folium
import pandas

map = folium.Map(location=[23.032179330323753, 72.44560476930867], zoom_start=6)

data = pandas.read_csv("india.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
nm = list(data["NAME"])

fg = folium.FeatureGroup("My Map")

for lt, lg, nm in zip(lat, lon, nm):
    fg.add_child(folium.Marker(location=[lt, lg], popup=nm, icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("map1.html")