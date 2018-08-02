from unittest import TestCase
import vivino.data.geojson.serialiser as ser

from vivino.data.model.winery import Winery

import json


class TestSerialise(TestCase):

    def test_serialise(self):

        serialised = ser.serialise(Winery("Alfred Bayer",17.0118954,45.5643442,2,"Red Wine"))

        jsonres = json.loads(serialised)

        self.assertEqual(jsonres['type'], 'Feature')

        self.assertEqual(jsonres['geometry']['type'], 'Point')

        self.assertEqual(jsonres['geometry']['coordinates'][0], 17.0118954)

        self.assertEqual(jsonres['geometry']['coordinates'][1], 45.5643442)

        self.assertEqual(jsonres['properties']['name'], 'Alfred Bayer')

        self.assertEqual(jsonres['properties']['count'], 2)

        self.assertEqual(jsonres['properties']['wine_type'], 'Red Wine')
