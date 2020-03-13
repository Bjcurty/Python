import folium
import pandas

def elev_color(el):
    if el <= 1500:
        return "green"
    elif el <= 3000:
        return "orange"
    else:
        return "red"

# print(dir(folium))
# print(help(folium.Map))

data = pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
names=list(data["NAME"])

# print(data.columns)
# print(data)
# print(len(lat))

map=folium.Map(location=[33,-112], zoom_start=5, tiles="OpenStreetMap")

fg1=folium.FeatureGroup(name="Volcanoes")
fg2=folium.FeatureGroup(name="Population")


for lt, ln, el, n in zip(lat, lon, elev, names):
    fg1.add_child(folium.CircleMarker(radius=7,location=[lt,ln],
    popup=n+"\n"+"Elevation: "+str(int(el))+"m", fill=True, fill_color=elev_color(el),
    color="gray",fill_opacity=0.7))

fg2.add_child(folium.GeoJson(data=open("world.json", 'r', encoding="utf-8-sig").read(),
style_function=lambda x:{"fillColor":"yellow" if x['properties']['POP2005'] < 10000000
else "green" if x['properties']['POP2005'] < 30000000
else "orange" if x['properties']['POP2005'] < 50000000
else "pink" if x['properties']['POP2005'] < 100000000
else "purple" if x['properties']['POP2005'] < 200000000
else "red"}))

map.add_child(fg2)
map.add_child(fg1)
map.add_child(folium.LayerControl())

map.save("Map1.html")
