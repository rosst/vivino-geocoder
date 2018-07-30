import pandas as pd

import helpers

import argparse

parser = argparse.ArgumentParser(description='Bulk geocode a Vivino export file in tsv format.')

parser.add_argument('--path', required=True, dest="path",
                    help='The path to the tsv file', type=lambda x: helpers.is_valid_file(x))

args = parser.parse_args()

data = pd.read_csv(args.path, sep='\t', header=0, encoding='utf8')

# Cache of geocoded regions
regions = {}

# Geocoded wine ids
geocoded = {}

# Geocode all unique countries in the list
countrycoords = helpers.geocode_list(data.Country.unique())

# Attempt to geocode each wine based on it's region
for i in data[['Region', 'Country']].itertuples():

    if isinstance(i.Region, str):

        region = i.Region + ' ' + i.Country

        # Check the cache first before querying Nominatim
        if region not in regions:

            coords = helpers.get_coordinates(region)

            regions[region] = coords

        else:

            coords = regions[region]

        # Fall back to using the country coordinates if the geocoder fails
        geocoded[i.Index] = coords if coords != (0, 0) else countrycoords[i.Country]

    else:
        # Fall back to using the country coordinates if no region information is provided in the data
        geocoded[i.Index] = countrycoords[i.Country]

    # Join the coordinates with the original data based on the index of the wine
geodf = pd.DataFrame.from_dict(geocoded, orient='index')

geodf.columns = ['lat', 'lon']

data = data.join(geodf)

print(data)