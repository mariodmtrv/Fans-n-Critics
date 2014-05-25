from imdbpie import *
from RatingEngine import RatingEngine
class IMDBRatingEngine(RatingEngine):
    """Represents the IMDB rating engine and its results for a movie"""
    def __init__(self, movie_id):
        self.__movie_id = movie_id
        imdb = Imdb()
        try: 
            movie = imdb.find_movie_by_id(self.__movie_id)
        except Exception:
            print("Movie was not found")
        self.__rating = movie.rating
        self.__votes = movie.votes
        self.__name = "IMDB"
        self.__logo = "resources/logos/imdb"
    def rating(self):
        return self.__rating
    def engine_logo(self):
        return self.__logo
    def engine_name(self):
        return self.__name
    def votes_count(self):
        return self.__votes