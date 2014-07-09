class ReviewProvider(object):

    """Collects the data from a review url and produces an evaluation result"""

    def __init__(self, article_url):
        self.__article_url = article_url
        self.__rating = 0

    @property
    def rating(self):
        return self.__rating

    def __article(self):
        '''
        Extracts the article text from the URL
        '''
        return self.__article()

    @property
    def article_url(self):
        return self.__article_url
