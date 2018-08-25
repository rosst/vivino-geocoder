import time

import json

import urllib.request

from vivino import utils


# Return a dict of from the given list of places that maps each place name to a pair of latitude longitude coordinates.

def geocode_list(places, referrer):

    querycache = set()

    lookup = {}

    for place in places:

        if place not in querycache:

            querycache.add(place)

            lookup[place] = get_coordinates(place, referrer)

            # Comply with https://operations.osmfoundation.org/policies/nominatim/
            time.sleep(1)

    return lookup


# Return a pair of latitude longitude coordinates for a given place name by querying the nominatim open street web_app
# API if no coordinates are found, <0,0> is returned.

def get_coordinates(place, referrer):

    if not isinstance(place, str):

        return 0, 0

    url = utils.encode_url('https://nominatim.openstreetmap.org/search/' + place + '?format=json&limit=1')

    try:

        req = urllib.request.Request(url)

        req.add_header('Referer', referrer)

        with urllib.request.urlopen(req) as response:

            if response.status != 200:

                raise Exception('Exception: HTTP response status is ' + str(response.status))

            jsonres = json.loads(response.read().decode('utf-8'))

            if len(jsonres) != 1 or not isinstance(jsonres, list):

                raise Exception('Exception: Bad JSON response format for place name ' + place)

            if 'lat' not in jsonres[0]:

                raise Exception('Exception: Bad JSON response format, no key named \'lat\' for place name ' + place)

            lat = jsonres[0]['lat']

            if 'lon' not in jsonres[0]:

                raise Exception('Exception: Bad JSON response format, no key named \'lon\' for place name ' + place)

            lon = jsonres[0]['lon']

    except Exception as e:

        print(e)

        return 0, 0

    return lat, lon
