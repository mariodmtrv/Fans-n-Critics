import unittest
from movie_data_extraction.ReviewProvision.ReviewCrawler import ReviewCrawler
import urllib
class ReviewCrawlerTest(unittest.TestCase):
    def test_search_url_extraction(self):
        '''
        Mocks an API response to test whether Search results URL extraction is correct
        '''
        r = ReviewCrawler()
        response_file = open('test_data/review_crawler_response.json','r')
        string_response = response_file.read()
        print(string_response)
        r.from_response(string_response)
        expected = 'http://www.rottentomatoes.com/m/monty_python_and_the_holy_grail/'
        actual= r.get_result_url(0)
        self.assertEqual(expected,actual)
if __name__ == '__main__':
    unittest.main()
