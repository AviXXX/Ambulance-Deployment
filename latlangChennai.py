import googlemaps, gmplot, webbrowser, os, json
import numpy as np
gmaps = googlemaps.Client(key='')

f = open('chennai.txt', 'r+')
listOfPlaces = f.readlines()
f.close()

n=len(listOfPlaces)
print(n)
latlng=[[0 for i in range(2)] for j in range(n)]
for i in range(n):
    print("in for")
    geocode_result = gmaps.geocode(listOfPlaces[i])
    #gmap1 = gmplot.GoogleMapPlotter.from_geocode("Surathkal")
    #print("geocode_result\n")
    #print(geocode_result)
    geom = geocode_result[0]['geometry']
    #print("geom\n")
    #print(geom)
    loc = geom['location']
    print("loc\n")
    print(loc)
    lat = loc['lat']
    lng = loc['lng']
    print(lat, lng)
    latlng[i][0]=lat
    latlng[i][1]=lng
    print(latlng[i][0], latlng[i][1], i)
    #gmap = gmplot.GoogleMapPlotter(lat, lng, 13)
    #hidden_gem_lat, hidden_gem_lon = lat,lng
    #gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')

a=np.array(latlng)
mat =np.matrix(a)
with open('LatitudeLongitudeChennai.txt','wb') as f:
    for line in mat:
        np.savetxt(f, line, fmt='%.8f')
print(latlng)
# Draw
#gmap.draw("my_map.html")

#filename = 'file:///'+os.getcwd()+'/' + 'my_map.html'
#webbrowser.open_new_tab(filename)
