# vivino-geocoder

The purpose of this Python repository is to bulk geocode a list of wines that can be exported from a www.vivino.com account, so that they can be displayed on a map using https://openlayers.org/. 

To get the software running in a docker container, perform the following steps:

1. Install Docker (https://docs.docker.com/install/) locally.
2. From the root directory of the project, run ```bash docker build -t geocoder .```.
3. Run the built container, binding port 5000 in the container to port 5000 on localhost ```bash docker container run -d -p 5000:5000  geocoder:latest```.
4. Run ```bash docker container ls``` to check the container is running.

The repository contains the following command line tools and web applications:

1. Flask web application on localhost:5000 (port can be changd when the docker container run command is specified), which displays the data file in vivino/web_app/static/data.json.

2. vivino/geocoder/bulk.py, which can be used to bulk geocode a Vivino export file in tsv format. This tool can be run from the command line as follows: 

```bash
docker exec -it [CONTAINERID] python vivino/geocoder/bulk.py --inputpath INPUTPATH --outputpath OUTPUTPATH  
```

What it does:

2.1. Loads a tsv file of wine data exported from a Vivino account.
2.2. Extracts the region / country information for each entry in the file
2.3. Queries the https://wiki.openstreetmap.org/wiki/Nominatim API with the extraxted region / country information
2.4. Extracts the latitude longitude from each response and updates the relevant wine entry in a new tsv file. 

3. vivino/geocoder/data/geojson/serialiser.py, which can take the output of vivino/geocoder/bulk.py and turn it into a http://geojson.org/ file, suitable for displaying it on a map using OpenLayers. This tool can be run from the command line as follows: 

```bash
docker exec -it [CONTAINERID] python vivino/data/geojson/serialiser.py --inputpath INPUTPATH --outputpath OUTPUTPATH
```

What it does:

3.1. Groups the geocode Vivino data by winery, using https://pandas.pydata.org/.
3.2. Serialises the data in GeoJson format, using https://pypi.org/project/Shapely/.
