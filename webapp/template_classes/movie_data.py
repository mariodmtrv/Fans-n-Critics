__author__ = 'mario-dimitrov'
from webapp.viewloaders.color_code_calc import generate_color_code
from webapp.models import Movie

from datetime import datetime

class MovieData(Movie):
        def __init__(self, db_movie):
            if db_movie.description == None:
                self.description = "No description available"
            else:
                self.description = db_movie.description

            if db_movie.genres == None:
                self.genres = "No genres available"
            else:
                self.genres = db_movie.genres

            if db_movie.poster == None:
                self.poster = "No poster available"
            else:
                self.poster = db_movie.poster
            if db_movie.released == None:
                self.released = datetime.date(1900, 1, 1)
            else:
                self.released = db_movie.released
            self.title = db_movie.title
            self.overall_rating = 3.7
            self.color_code = generate_color_code(self.overall_rating)