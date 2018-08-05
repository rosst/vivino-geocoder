import unittest

from vivino.utils import encode_url, is_valid_file

from argparse import ArgumentTypeError


class TestUtils(unittest.TestCase):

    def test_encode_url(self):

        to_encode = 'https://nominatim.openstreetmap.org/search/médoc?format=json&limit=1'

        encoded = 'https://nominatim.openstreetmap.org/search/m%C3%A9doc?format=json&limit=1'

        self.assertEqual(encode_url(to_encode), encoded)

    def test_is_valid_file(self):

        self.assertRaises(ArgumentTypeError, is_valid_file, 'test')


if __name__ == '__main__':
    unittest.main()
