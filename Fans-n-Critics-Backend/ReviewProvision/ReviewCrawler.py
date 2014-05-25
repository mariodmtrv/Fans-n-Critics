from google_search import *
class ReviewCrawler():
    """Crawls Google for reviews of the movie and adds them to the database"""
    def __init__(self, query):
        self.__query = query
        g = pygoogle(query)
    def get_queries():
         return g.get_result_count()


