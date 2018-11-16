import googlemaps

# Requires API key
gmaps = googlemaps.Client(key='')

# Requires cities name
my_dist = gmaps.distance_matrix('madya','dodda kopla')['rows'][0]['elements'][0]

# Printing the result
print(my_dist)
