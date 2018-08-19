# vivino-geocoder
Geocode entries in a tsv export of Vivino data.

The purpose of this Python script is to bulk geocode a list of wines exported from a www.vivino.com account, so that they can be displayed on a map. 

The script performs the following tasks:

1. Loads a tsv file of wine data exported from a Vivino account.
2. Extracts the region / country information for each entry in the file
3. Queries the https://wiki.openstreetmap.org/wiki/Nominatim API with the extraxted region / country information
4. Extracts the latitude longitude from each response and updates the relevant wine entry in a new tsv file. 

Run flask web application on localhost:5000:

1. docker build -t geocoder .
2. docker container run -d -p 5000:5000  geocoder:latest

