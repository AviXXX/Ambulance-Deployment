
# import gmplot package
import gmplot

# GoogleMapPlotter return Map object
# Pass the center latitude and
# center longitude
lat=30.3164945
lng=78.03219179999999
gmap1 = gmplot.GoogleMapPlotter(lat, lng, 13 )

# Pass the absolute path
gmap1.draw( "home\\map11.html" )
