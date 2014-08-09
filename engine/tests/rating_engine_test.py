__author__ = 'mario-dimitrov'

import unittest

from engine.rating_engines.imdb_rating_engine import IMDBRatingEngine


class IMDBTest(unittest.TestCase):
    def test_rating_extraction(self):
        engine = IMDBRatingEngine('tt0071853')
        expected_rating = 8.4
        actual_rating = engine.rating()
        expected_votes = 293275
        actual_votes = engine.votes_count()
        self.assertEqual(expected_rating, actual_rating)
        self.assertEqual(expected_votes, actual_votes)


if __name__ == '__main__':
    unittest.main()
