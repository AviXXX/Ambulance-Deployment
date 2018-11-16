import numpy as np
import gmplot
import googlemaps, gmplot, webbrowser, os, json
import gmaps
import ipywidgets.embed
gmaps.configure(api_key='')
marker_locations = [
    (-34.0, -59.166672),
    (-32.23333, -64.433327),
    (40.166672, 44.133331),
    (51.216671, 5.0833302),
    (51.333328, 4.25)
]

fig = gmaps.figure()
markers = gmaps.marker_layer(marker_locations)
fig.add_layer(markers)
fig
embed_minimal_html('export.html', views=[fig])
