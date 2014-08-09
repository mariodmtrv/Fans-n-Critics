import re

from bs4 import BeautifulSoup
import requests


class ReviewParser():
    """Extracts the text from an html page, containing a review
       Really simple implementation, many paths of improvement
    """

    @staticmethod
    def extract_review_words(page_html):
        html_page = ReviewParser.__extract_review_data(page_html)
        words = ReviewParser.__extract_words(html_page)
        return words

    def extract_page(self, review_url):
        req = requests.get(review_url)
        if req.status_code == 200:
            self.__review_date = req.headers['Date'][5:16]
        else:
            self.__review_date = 'Unknown'

        if req.status_code == 200:
            return req.text

        raise "Failed to extract page"

    def get_result_date(self):
        return self.__review_date

    @staticmethod
    def __visible(element):
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title', 'iframe']:
            return False
        elif re.match('<!--.*-->', str(element)):
            return False
        return True

    @staticmethod
    def __extract_review_data(page_html):
        parser = BeautifulSoup(page_html)
        texts = parser.body.findAll(text=True)
        visible_texts = filter(ReviewParser.__visible, texts)
        return list(visible_texts)

    @staticmethod
    def __extract_words(texts):
        #Extracts the tokens from every element
        result = map(lambda text: text.split(), texts)
        tokenized_lists = list(result)
        # Flattens the list
        merged_list = [item for sublist in tokenized_lists for item in sublist]
        _digits = re.compile('\d')

        # Does not contain simple stopwords or digits
        words_list = [item for item in merged_list if len(item) > 2 and not bool(_digits.search(item))]
        return list(words_list)







