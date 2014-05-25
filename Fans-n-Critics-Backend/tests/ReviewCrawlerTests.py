import unittest
from ReviewCrawler import ReviewCrawler
class Test_test1(unittest.TestCase):
    def test_crawling(self):
        r = ReviewCrawler("django unchained")
        print()
       
if __name__ == '__main__':
    unittest.main()
