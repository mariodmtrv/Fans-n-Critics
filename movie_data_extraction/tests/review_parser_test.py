import unittest
from movie_data_extraction.review_provision.review_parser import ReviewParser

__author__ = 'mario-dimitrov'


class ReviewCrawlerTest(unittest.TestCase):
    def extract_page(self):
        ReviewParser.extract_review_page("http://www.rottentomatoes.com/m/monty_python_and_the_holy_grail/")