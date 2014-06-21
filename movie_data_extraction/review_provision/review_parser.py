import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
class ReviewParser():
    """Extracts the text from an html page, containing a review"""
    @staticmethod
    def extract_review(review_url):
        page_content = urllib.request.urlopen(review_url)
        page_html = page_content.read().decode("utf8")
        parser = BeautifulSoup(page_html)
        str_list = []
        print(str(review_url).capitalize())
        for element in parser.body:
                string_element = str(element)
                if(not (string_element.startswith("<script>"))):
                    logical_element = BeautifulSoup(string_element)
                    for content in logical_element.stripped_strings:
                        str_list.append(repr(content))
        return ''.join(str_list)
