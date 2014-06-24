import datetime
import re
from  movie_data_extraction.APIs.imdb.imdbpie import Imdb


class DescriptionProvider():
    """Defines the provider of the movie description"""

    def __init__(self, movie_id):
        self.__movie_id = movie_id
        imdb = Imdb()
        movie = imdb.find_movie_by_id(self.__movie_id)
        self.__title = movie.title
        self.__description = movie.plot_outline
        self.__genres = movie.genres
        self.__poster = movie.poster_url
        released = self.__get_released_date(movie)
        self.__released = datetime.date(int(released[0]),int(released[1]),int(released[2]))

    @staticmethod
    def __get_released_date(movie):
        released_string = movie.release_date
        match=re.findall(r'(\d+)',released_string)
        return match

    def get_name(self):
        return self.__title

    def get_short_description(self):
        return self.__description

    def get_genre_list(self):
        return self.__genres

    def get_poster_url(self):
        return self.__poster

    def get_released(self):
        return self.__released
