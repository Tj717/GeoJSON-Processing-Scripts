#! usr/bin/env python
import json 

# Path for file to be converted
in_file = ''

# Path for file storing converted GeoJSON
out_file = ''

# Type of geometry
geo_type = ''

data = json.load(open(in_file))

geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": geo_type,
            "coordinates": [d["Longitude"], d["Latitude"]],
            },
        "properties" : d,
     } for d in data]
}

output = open(out_file, 'w')
json.dump(geojson, output)