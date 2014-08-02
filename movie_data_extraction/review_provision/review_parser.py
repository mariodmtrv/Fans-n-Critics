import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import requests


class ReviewParser():
    """Extracts the text from an html page, containing a review"""

    @staticmethod
    def extract_review_page(review_url):
        req = requests.get(review_url)
        print(req['Status'])
        return req

    @staticmethod
    def extract_review(page_html):
        parser = BeautifulSoup(page_html)
        str_list = []
        for element in parser.body:
            string_element = str(element)
            if (not (string_element.startswith("<script>"))):
                logical_element = BeautifulSoup(string_element)
                for content in logical_element.stripped_strings:
                    str_list.append(repr(content))
        return ''.join(str_list)
