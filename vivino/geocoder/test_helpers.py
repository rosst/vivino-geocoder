import unittest

from unittest import TestCase, mock

from unittest.mock import MagicMock

from http.client import HTTPResponse

from vivino.geocoder.helpers import get_coordinates


class TestHelpers(TestCase):

    @mock.patch('helpers.urllib.request.urlopen')
    def test_get_coordinates_valid_json_response(self, mocked_request):

        response_json = '[{"place_id": "94242929", "licence": "Data © OpenStreetMap contributors, ODbL 1.0. ' \
                        'https://osm.org/copyright", "osm_type": "way", "osm_id": "114823817", "boundingbox": ' \
                        '["51.1525635", "51.1614997", "-1.4508447", "-1.4408037"], "lat": 51.1576661, "lon": ' \
                        '-1.4458572, "display_name": "Test, Test Valley, Hampshire, South East, England, SO20 6BD,' \
                        ' UK", "class": "waterway", "type": "river", "importance": 0.46204844474975}]'

        a = MagicMock(status=200)

        b = MagicMock()

        b.decode.return_value = response_json

        a.read.return_value = b

        mocked_request.return_value.__enter__.return_value = a

        coords = get_coordinates('test')

        self.assertEqual(coords, (51.1576661, -1.4458572))

    @mock.patch('helpers.urllib.request.urlopen')
    def test_get_coordinates_bad_json_response(self, mocked_request):

        a = MagicMock(status=200)

        b = MagicMock()

        b.decode.return_value = '{"test":1}'

        a.read.return_value = b

        mocked_request.return_value.__enter__.return_value = a

        coords = get_coordinates('test')

        self.assertEqual(coords, (0, 0))

    @mock.patch('helpers.urllib.request.urlopen')
    def test_get_coordinates_bad_http_status(self, mocked_request):

        a = MagicMock(status=300)

        mocked_request.return_value.__enter__.return_value = a

        coords = get_coordinates('test')

        self.assertEqual(coords, (0, 0))

    @mock.patch('helpers.urllib.request.urlopen')
    def test_get_coordinates_missing_lat(self, mocked_request):

        response_json = '[{"place_id": "94242929", "licence": "Data © OpenStreetMap contributors, ' \
                        'ODbL 1.0. https://osm.org/copyright", "osm_type": "way", "osm_id": "114823817", ' \
                        '"boundingbox": ["51.1525635", "51.1614997", "-1.4508447", "-1.4408037"], "lon": -1.4458572, ' \
                        '"display_name": "Test, Test Valley, Hampshire, South East, England, SO20 6BD, UK", ' \
                        '"class": "waterway", "type": "river", "importance": 0.46204844474975}]'

        a = MagicMock(status=200)

        b = MagicMock()

        b.decode.return_value = response_json

        a.read.return_value = b

        mocked_request.return_value.__enter__.return_value = a

        coords = get_coordinates('test')

        self.assertEqual(coords, (0, 0))

    @mock.patch('helpers.urllib.request.urlopen', spec=HTTPResponse)
    def test_get_coordinates_missing_lon(self, mocked_request):

        response_json = '[{"place_id": "94242929", "licence": "Data © OpenStreetMap contributors, ODbL 1.0. ' \
                        'https://osm.org/copyright", "osm_type": "way", "osm_id": "114823817", "boundingbox": ' \
                        '["51.1525635", "51.1614997", "-1.4508447", "-1.4408037"], "lat": 51.1576661, ' \
                        '"display_name": "Test, Test Valley, Hampshire, South East, England, SO20 6BD, UK", "class": ' \
                        '"waterway", "type": "river", "importance": 0.46204844474975}]'

        a = MagicMock(status=200)

        b = MagicMock()

        b.decode.return_value = response_json

        a.read.return_value = b

        mocked_request.return_value.__enter__.return_value = a

        coords = get_coordinates('test')

        self.assertEqual(coords, (0, 0))


if __name__ == '__main__':

    unittest.main()
