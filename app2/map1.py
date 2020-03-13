# Brad Curtis
# 3/12/2020
# Program to create a map object that is interactive with user. Need expanding for usability
# Inluenced by The Python Mega Course taught by Ardit Sulce
import folium
import pandas

# This method is to select a color for volcanoe circles based on height
def elev_color(el):
    if el <= 1500:
        return "green"
    elif el <= 3000:
        return "orange"
    else:
        return "red"

# importing of a txt file to use data for program. Lists are used as they are faster than
# dataframes for computing
data = pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
names=list(data["NAME"])

# creating a map for a base to work
map=folium.Map(location=[33,-112], zoom_start=5, tiles="OpenStreetMap")

# using feature groups to be added later to the map in layers
fg1=folium.FeatureGroup(name="Volcanoes")
fg2=folium.FeatureGroup(name="Population")

# this loop adds a circle marker for each volcano split among the 4 lists.
for lt, ln, el, n in zip(lat, lon, elev, names):
    fg1.add_child(folium.CircleMarker(radius=7,location=[lt,ln],
    popup=n+"\n"+"Elevation: "+str(int(el))+"m", fill=True, fill_color=elev_color(el),
    color="gray",fill_opacity=0.7))

# Here, an overlay is being developed to trace each country and then color code it based on population
fg2.add_child(folium.GeoJson(data=open("world.json", 'r', encoding="utf-8-sig").read(),
style_function=lambda x:{"fillColor":"yellow" if x['properties']['POP2005'] < 10000000
else "green" if x['properties']['POP2005'] < 30000000
else "orange" if x['properties']['POP2005'] < 50000000
else "pink" if x['properties']['POP2005'] < 100000000
else "purple" if x['properties']['POP2005'] < 200000000
else "red"}))

# here the featuregroups are being added to the map along with layer control. fg2 is added before fg1
# so that the circles can still be clicked on without disabling layer from fg2
map.add_child(fg2)
map.add_child(fg1)
map.add_child(folium.LayerControl())

# This saves our map from the program to a local document
map.save("Map1.html")
