from unittest import TestCase

import vivino.data.geojson.serialiser as ser

from vivino.data.model.winery import Winery

from shapely_geojson import Feature

from shapely.geometry import Point

import json


class TestSerialiser(TestCase):

    def test_serialise(self):

        serialised = ser.serialise(Winery("Alfred Bayer", 17.0118954, 45.5643442, 2))

        jsonres = json.loads(serialised)

        self.assertEqual(jsonres['type'], 'Feature')

        self.assertEqual(jsonres['geometry']['type'], 'Point')

        self.assertEqual(jsonres['geometry']['coordinates'][0], 45.5643442)

        self.assertEqual(jsonres['geometry']['coordinates'][1], 17.0118954)

        self.assertEqual(jsonres['properties']['name'], 'Alfred Bayer')

        self.assertEqual(jsonres['properties']['count'], 2)


    def test_create_feature(self):

        feature = ser.create_feature(Winery("Alfred Bayer", 17.0118954, 45.5643442, 2))

        self.assertTrue(isinstance(feature, Feature))

        self.assertEqual(feature.properties['name'], 'Alfred Bayer')

        self.assertEqual(feature.properties['count'], 2)

        self.assertTrue(isinstance(feature.geometry, Point))

        self.assertEqual(feature.geometry.coords[0], (45.5643442, 17.0118954))
