import googlemaps
import numpy as np
#import requests, json

# Requires API key
gmaps = googlemaps.Client(key='')

f = open('Region9.txt', 'r+')
lis = f.readlines()
f.close()

'''
size=len(lines)
i=0
j=0
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
while i < size:
    source = lines[i]
    while j < size:
        destination = lines[j]
        r=requests.get(url+'origins = ' + source +
                            '&destinations = '+ destination +
                            '&key = ' + api_key)

        x = r.json()
        # Requires cities name
        #my_dist[list].append(gmaps.distance_matrix('marathalli','electroniccity')['rows'][0]['elements'][0])
        # Printing the result
        print(x)
        j=j+1
    i=i+1
'''

n=len(lis)
print(n)
dist=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):

        my_dist = gmaps.distance_matrix(lis[i],lis[j])['rows'][0]['elements'][0]
        #if((my_dist['distance']['value'])!= None):
        dist[i][j]=my_dist['distance']['value']/1000
        print(dist[i][j], j)
        #print(my_dist)
    #print('\n')
a=np.array(dist)
mat =np.matrix(a)
with open('pathRegion9.txt','wb') as f:
    for line in mat:
        np.savetxt(f, line, fmt='%d')
print(dist)
