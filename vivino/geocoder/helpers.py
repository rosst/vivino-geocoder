import json

from urllib import request

from vivino import utils


# Return a dict of from the given list of places that maps each place name to a pair of latitude longitude coordinates.

def geocode_list(places):

    querycache = set()

    lookup = {}

    for place in places:

        if place not in querycache:

            querycache.add(place)

            lookup[place] = get_coordinates(place)

    return lookup


# Return a pair of latitude longitude coordinates for a given place name by querying the nominatim open street web_app
# API if no coordinates are found, <0,0> is returned.

def get_coordinates(place):

    url = utils.encode_url('https://nominatim.openstreetmap.org/search/' + place + '?format=json&limit=1')

    try:

        with request.urlopen(url) as response:

            jsonres = json.loads(response.read().decode('utf-8'))

            if len(jsonres) == 0:
                return 0, 0

            lat = jsonres[0]['lat']

            lon = jsonres[0]['lon']

    except Exception as e:

        print("type error: " + str(e))

        return 0, 0

    return lat, lon
