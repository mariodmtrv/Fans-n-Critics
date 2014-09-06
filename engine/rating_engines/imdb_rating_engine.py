from engine.APIs.imdb.imdbpie import Imdb
from engine.rating_engines.rating_engine import RatingEngine


class IMDBRatingEngine(RatingEngine):
    """Represents the IMDB rating engine and its results for a movie"""

    def __init__(self, movie_id):
        # RatingEngine.__init__(self)
        self.__movie_id = movie_id
        imdb = Imdb()
        try:
            movie_data = imdb.find_movie_by_id(self.__movie_id)
            self.__rating = movie_data.rating
            self.__votes = movie_data.votes
            self.__name = "IMDB"
            self.__logo = "http://www.cinephreakpictures.com/images/imdb_logo_small.png"
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
