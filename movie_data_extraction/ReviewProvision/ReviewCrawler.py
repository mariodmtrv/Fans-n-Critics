from movie_data_extraction.Parsers.xgoogle.search import GoogleSearch


class ReviewCrawler():
    """Crawls Google for reviews of the movie and adds them to the database"""

    def __init__(self, query):
        self.__query = query
        self.__search_instance = GoogleSearch("hello")
        self.__search_instance.results_per_page = 50
        self.__results = self.__search_instance.get_results();

    def get_queries(self):
        return self.__results


