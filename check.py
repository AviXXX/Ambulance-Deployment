import googlemaps, gmplot, webbrowser, os, json
gmaps = googlemaps.Client(key='')
geocode_result = gmaps.geocode("Surathkal,India")
#gmap1 = gmplot.GoogleMapPlotter.from_geocode("Surathkal")
print("geocode_result\n")
print(geocode_result)
geom = geocode_result[0]['geometry']
print("geom\n")
print(geom)
loc = geom['location']
print("loc\n")
print(loc)
lat = loc['lat']
lng = loc['lng']
print(lat, lng)
gmap = gmplot.GoogleMapPlotter(lat, lng, 13)
hidden_gem_lat, hidden_gem_lon = lat,lng
gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')

# Draw
gmap.draw("my_map.html")

filename = 'file:///'+os.getcwd()+'/' + 'my_map.html'
webbrowser.open_new_tab(filename)
