import unittest
import os

from engine.review_provision.review_ranker import ReviewRanker


__author__ = 'mario-dimitrov'


class ReviewRankerTest(unittest.TestCase):
    def test_calculate_review_rank(self):
        dir = os.path.dirname(__file__)
        review_words_filepath = os.path.join(
            dir, "test_data/parsed_review_words.txt")
        with open(review_words_filepath, 'r') as review_words_file:
            words_raw_list = review_words_file.read()[1:-1].split()
            words = [word[1:-2] for word in words_raw_list]
            ranker = ReviewRanker(words)
            self.assertEqual(7.1, ranker.calculate_review_rank())


if __name__ == '__main__':
    unittest.main()
