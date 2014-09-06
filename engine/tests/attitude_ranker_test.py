import unittest

from engine.review_provision.attitude_ranker import AttitudeRanker


__author__ = 'mario-dimitrov'


class AttitudeRankerTest(unittest.TestCase):
    def test_calculate_word_attitude(self):
        ranker = AttitudeRanker()
        self.assertEqual(
            AttitudeRanker.POSITIVE, ranker.categorize_word("nice"))
        self.assertEqual(
            AttitudeRanker.NEGATIVE, ranker.categorize_word("awkwardness"))
        self.assertEqual(
            AttitudeRanker.NOT_RATED, ranker.categorize_word("normal"))


if __name__ == '__main__':
    unittest.main()
