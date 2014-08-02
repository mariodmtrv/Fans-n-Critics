import unittest
import os
from movie_data_extraction.review_provision.attitude_ranker import AttitudeRanker
from movie_data_extraction.review_provision.review_parser import ReviewParser

__author__ = 'mario-dimitrov'


class AttitudeRankerTest(unittest.TestCase):
    def test_calculate_word_attitude(self):
        ranker = AttitudeRanker()
        print(ranker.categorize_word("nice"))
        print(ranker.categorize_word("awkwardness"))
        print(ranker.categorize_word("normal"))

        ranker.categorize_word()


if __name__ == '__main__':
    unittest.main()