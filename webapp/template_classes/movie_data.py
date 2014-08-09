__author__ = 'mario-dimitrov'

import urllib.request
import shutil
from datetime import datetime

from webapp.viewloaders.color_code_calc import generate_color_code
from engine.rating_engines.imdb_rating_engine import IMDBRatingEngine
from webapp.models import Movie


URL = "/static/resources/movie_posters/"


class MovieData(Movie):
    def __init__(self, db_movie):
        if db_movie.description is None:
            self.description = "No description available"
        else:
            self.description = db_movie.description

        if db_movie.genres is None:
            self.genres = "No genres available"
        else:
            self.genres = db_movie.genres

        if db_movie.released is None:
            self.released = datetime.date(1900, 1, 1)
        else:
            self.released = db_movie.released

        if db_movie.poster is None:
            db_movie.poster = ""
        else:
            "Loads the image from the url and stores it to the system storage"
            image_url = db_movie.title + db_movie.released.strftime('%m%d%Y') + ".jpg"
            with urllib.request.urlopen(db_movie.poster) as response, open("webapp" + URL + image_url,
                                                                           'wb') as out_file:
                shutil.copyfileobj(response, out_file)
            self.poster = image_url

        self.title = db_movie.title
        x = IMDBRatingEngine(db_movie.movie_id)
        self.overall_rating = (x.rating())
        self.color_code = generate_color_code(self.overall_rating)