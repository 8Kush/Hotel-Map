# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 13:30:09 2018

@author: Lenovo
"""

import folium
import pandas
data = pandas.read_csv("hotel.csv")
lat = list(data["latitude"])
lon = list(data["longitude"])
add = list(data["address"])
room = list(data["room_count"])

def color_producer(rooms):
    if rooms < 10:
        return 'green'
    elif 10 <= rooms < 20:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[26.8, 75.7], zoom_start=5, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Hotels")

fg = folium.FeatureGroup(name="My Loc")
for lt, ln, ad, ro in zip(lat, lon, add, room):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(ad), 
                                     fill_color=color_producer(ro), fill=True, color='grey', fill_opacity=0.7)) 
    
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
                                     
map.save("Map1.html")