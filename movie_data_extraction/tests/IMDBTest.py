__author__ = 'mario-dimitrov'

import unittest
from RatingEngines.IMDBRatingEngine import IMDBRatingEngine

class IMDBTest(unittest.TestCase):
    def test_rating_extraction(self):
        engine = IMDBRatingEngine('tt0071853')
        #'tt0071853'
        # print(engine.rating())
        #self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
