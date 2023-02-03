import json

# Path for file to be processed~
file = ''

# Path for file storing processed JSON
new_file = ''

# Names of fields to be removed
fields_remove = [
    ''
]

jsonfile = open(file)
data = json.load(jsonfile)

# for GeoJSON files with properties
for  i in range(len(data['features'])):
    for j in range(len(fields_remove)):
        del data['features'][i]['properties'][fields_remove[j]];

# for regular JSON files
# for  i in range(len(data)):
#     for j in range(len(fields_remove)):
#         del data[i][fields_remove[j]];

# Write processed JSON to a new file
open(new_file, "w").write(
    json.dumps(data, indent=4, separators=(',', ': '))
)
