__author__ = 'mario-dimitrov'

import unittest
from movie_data_extraction.movie_finder.description_provider import DescriptionProvider
import datetime


class DescriptionProviderTest(unittest.TestCase):

    def test_movie_name_extraction(self):
        provider = DescriptionProvider("tt0071853")
        actual = provider.get_name()
        expected = 'Monty Python and the Holy Grail'
        self.assertEqual(actual, expected)

    def test_movie_genres_extraction(self):
        provider = DescriptionProvider("tt0071853")
        actual = provider.get_genre_list()
        expected = ['Adventure', 'Comedy', 'Fantasy']
        self.assertEqual(actual, expected)

    def test_released_parse(self):
        provider = DescriptionProvider("tt0071853")
        actual = provider.get_released()
        expected = datetime.date(1975, 5, 25)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
