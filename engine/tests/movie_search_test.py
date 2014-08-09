__author__ = 'mario-dimitrov'
import unittest

from engine.movie_finder.movie_search import MovieSearch


class MovieSearchTest(unittest.TestCase):
    def test_find_by_name_few_results_ask_for_too_many(self):
        finder = MovieSearch()
        actual = finder.get_alternatives_list(
            "Monty Python & the Holy Grail Location Report", 40000)
        expected = [{'title': 'Monty Python & the Holy Grail Location Report', 'year': '1974', 'imdb_id': 'tt0372432'},
                    {'title': 'Monty Python & the Holy Grail in Lego',
                     'year': '2001', 'imdb_id': 'tt0353751'},
                    {'title': 'Monty Python and the Holy Grail',
                     'year': '1975', 'imdb_id': 'tt0071853'},
                    {'title': 'Monty Python & the Quest for the Holy Grail', 'year': '1996', 'imdb_id': 'tt0151625'}]
        print(expected[0].get('title'))
        self.assertEqual(actual, expected)

    def test_find_by_name_no_results(self):
        finder = MovieSearch()
        actual = finder.get_alternatives_list("AlTa543DSccsaew")
        expected = []
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
