import argparse

import pandas as pd

import codecs

from shapely.geometry import Point

from shapely_geojson import dumps, Feature, FeatureCollection

from vivino import utils

from vivino.data.model.winery import Winery


def create_feature(winery):

    return Feature(Point(winery.coordinate[0], winery.coordinate[1]), properties={'name': winery.name, 'count': winery.count})


def serialise(winery):

    feature = Feature(Point(winery.coordinate[0], winery.coordinate[1]), properties={'name': winery.name, 'count': winery.count})

    return dumps(feature, indent=2)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Serialise tsv entries into winery json objects.')

    parser.add_argument('--inputpath', required=True, dest="inputpath",
                    help='The path to the input tsv file', type=lambda x: utils.is_valid_file(x))

    parser.add_argument('--outputpath', required=True, dest="outputpath",
                    help='The path to the output json file')

    args = parser.parse_args()

    data = pd.read_csv(args.inputpath, sep='\t', header=0, encoding='utf8')

    grouped = data[['Winery', 'lat', 'lon']].groupby(['Winery', 'lat', 'lon']).size().reset_index(name='count')

    features = list()

    for i in grouped.itertuples():

        nextwinery = Winery(i[1], float(i[2]), float(i[3]), i[4])

        nextfeature = create_feature(nextwinery)

        features.append(nextfeature)

    feature_collection = FeatureCollection(features)

    json = dumps(feature_collection, indent=2, ensure_ascii=False)

    with codecs.open(args.outputpath, 'w', encoding="utf-8") as outfile:

        outfile.write(json)
