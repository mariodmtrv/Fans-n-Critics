import unittest
from movie_data_extraction.review_provision.review_crawler import ReviewCrawler
from urllib.request import Request, urlopen
import os
import requests


class ReviewCrawlerTest(unittest.TestCase):

    def test_search_url_extraction(self):
        '''
        Mocks an API response to test whether Search results URL extraction is correct
        '''
        crawler = ReviewCrawler()

        dir = os.path.dirname(__file__)
        filepath = os.path.join(dir, "test_data/review_crawler_response.json")

        with open(filepath, 'r') as response_file:
            string_response = response_file.read()
            crawler.from_response(string_response)
            expected = 'http://www.rottentomatoes.com/m/monty_python_and_the_holy_grail/'
            actual = crawler.get_result_url(0)
            self.assertEqual(expected, actual)

    def test_url_f(self):
        req = requests.get('http://www.rottentomatoes.com/m/monty_python_and_the_holy_grail/')
        #req = Request('http://www.rottentomatoes.com/m/monty_python_and_the_holy_grail/')
        #webpage = urlopen(req).read()
        print(req.status_code)
        #info=response.info()
        #return info['Date']


if __name__ == '__main__':
    unittest.main()
