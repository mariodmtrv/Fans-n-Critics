__author__ = 'mario-dimitrov'

import unittest
from movie_data_extraction.tests.review_parser_test import ReviewParserTest
from movie_data_extraction.tests.review_crawler_test import ReviewCrawlerTest
from movie_data_extraction.tests.attitude_ranker_test import AttitudeRankerTest
from movie_data_extraction.tests.review_ranker_test import ReviewRankerTest


def suite():
    suite = unittest.TestSuite()
    suite.addTests(ReviewParserTest(), ReviewRankerTest(), AttitudeRankerTest(), ReviewCrawlerTest())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()

    test_suite = suite()

    runner.run(test_suite)