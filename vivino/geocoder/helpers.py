import json

from urllib import request
from urllib import parse

from argparse import ArgumentTypeError

# Check for valid file paths provided as command line arguments
# Following https://stackoverflow.com/questions/27494400/python-using-file-handle-to-print-contents-of-file


def is_valid_file(arg):

    try:

        return open(arg, 'r')  # return an open file handle

    except IOError:

        raise ArgumentTypeError("The file %s does not exist!" % arg)


# Encode non ascii charaters in a url
# Tip of the hat to
# https://stackoverflow.com/questions/4389572/how-to-fetch-a-non-ascii-url-with-python-urlopen/29231552


def encode_url(url):

    url = parse.urlsplit(url)

    url = list(url)

    url[2] = parse.quote(url[2])

    url = parse.urlunsplit(url)

    return url


# Return a dict of from the given list of places that maps each place name to a pair of latitude longitude coordinates.

def geocode_list(places):

    querycache = set()

    lookup = {}

    for place in places:

        if place not in querycache:

            querycache.add(place)

            lookup[place] = get_coordinates(place)

    return lookup


# Return a pair of latitude longitude coordinates for a given place name by querying the nominatim open street map API
# If no coordinates are found, <0,0> is returned.

def get_coordinates(place):

    url = encode_url('https://nominatim.openstreetmap.org/search/' + place + '?format=json&limit=1')

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
