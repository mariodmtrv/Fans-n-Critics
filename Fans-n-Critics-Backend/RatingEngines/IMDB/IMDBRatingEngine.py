from imdbpie import *
class IMDBRatingEngine(RatingEngine):
    """Represents the IMDB rating engine and its results"""
    def __init__(self, movie_id):
        self.__movie_id = movie_id
        imdb = Imdb()
        movie = imdb.find_movie_by_id(self.__movie_id)
        self.__rating = movie.rating
        self.__votes = movie.votes
        self.__name = "IMDB"
        self.__logo = "http://imdb.com/"