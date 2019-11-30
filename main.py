import folium,pandas
def markerColor(elevation):
    if elevation<1500:
        return 'green'
    elif elevation<3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.523, -122.675], titles="Mapbox Bright", zoom_start=3 )
fg_volcanoes = folium.FeatureGroup('Valcanoes')
fg_population = folium.FeatureGroup('Population')
volcanoes = pandas.read_csv('Volcanoes.txt')
lat = list(volcanoes['LAT'])
lon = list(volcanoes['LON'])
elev = list(volcanoes['ELEV'])
for i,j,k in zip(lat,lon,elev):
    # fg.add_child(folium.Marker([38.3,-110.90],popup='arun', icon=folium.Icon(color='black', icon_color='green', icon='info-sign', )))
    fg_volcanoes.add_child(folium.CircleMarker([i,j],radius=6, tooltip=str(k)+' m', color=markerColor(k), fill=True, fillOpacity=0.7, opacity=0.8, popup=folium.Popup()  ))
fg_population.add_child(folium.GeoJson(open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] <= 100000000 else 'red'}))
map.add_child(fg_volcanoes)
map.add_child(fg_population)
map.add_child(folium.LayerControl())
map.save('Map.html')