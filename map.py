from typing import List
import folium
import pandas

map = folium.Map(location=[23.032179330323753,
                 72.44560476930867], zoom_start=6)

data = pandas.read_csv("india.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
nm = list(data["NAME"])
html = """Location name:<br><a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a>"""


fg = folium.FeatureGroup("My Map")

# Used for simple popup info

# for lt, lg, nm in zip(lat, lon, nm):
#     fg.add_child(folium.Marker(location=[lt, lg], popup=nm, icon=folium.Icon(color="green")))

# Used for html popup
for lt, lg, nm in zip(lat, lon, nm):
    iframe = folium.IFrame(html=html % (nm, nm), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, lg], popup=folium.Popup(
        iframe), icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("mymap.html")
