import unittest
import os

from engine.review_provision.review_parser import ReviewParser


__author__ = 'mario-dimitrov'


class ReviewParserTest(unittest.TestCase):
    def test_extract_page_words(self):
        dir = os.path.dirname(__file__)
        html_page_filepath = os.path.join(dir, "test_data/review_parser_test_page.html")
        with open(html_page_filepath, 'r') as test_file:
            page = test_file.read()
            expected_result_filepath = os.path.join(dir, "test_data/parsed_review_words.txt")
            with open(expected_result_filepath) as expected_result:
                self.assertEqual(str(expected_result.read()), str(ReviewParser.extract_review_words(page)))


if __name__ == '__main__':
    unittest.main()