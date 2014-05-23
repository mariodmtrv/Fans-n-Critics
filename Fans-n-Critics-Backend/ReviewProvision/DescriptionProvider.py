from imdbpie import *
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
    def get_name(self):
        return self.__title
    def get_short_description(self): 
        return self.__description
    def get_genre_list(self):
        return self.__genres
    def get_poster_url(self):
        return self.__poster
