from movie_data_extraction.APIs.imdb.imdbpie import Imdb


class MovieSearch():
    """Processes a query to match it to a movie"""

    def __init__(self):
        self.__imdb = Imdb()

    def get_alternatives_list(self, movie_name, alt_count=5):
        result = self.__imdb.find_by_title(movie_name)
        if (len(result) > alt_count):
            return result[:alt_count]
        return result
