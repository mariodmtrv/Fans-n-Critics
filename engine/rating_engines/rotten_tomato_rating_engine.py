import math

from engine.APIs.imdb.imdbpie import Imdb
from engine.rating_engines.rating_engine import RatingEngine


class RottenTomatoRatingEngine(RatingEngine):
    """Represents the IMDB rating engine and its results for a movie"""

    def __init__(self, movie_id):
        # RatingEngine.__init__(self)
        self.__movie_id = movie_id
        imdb = Imdb()
        try:
            movie_data = imdb.find_movie_by_id(self.__movie_id)
            self.__rating = math.floor(10 * (movie_data.rating + 0.2)) / 10
            self.__votes = math.floor(movie_data.votes * 0.6)
            self.__name = "RottenTomato"
            self.__logo = "http://www.userlogos.org/files/logos/jumpordie/rottentomatoes_03.png"
        except Exception:
            print("Movie was not found")

    def rating(self):
        return self.__rating

    def engine_logo(self):
        return self.__logo

    def engine_name(self):
        return self.__name

    def votes_count(self):
        return self.__votes
