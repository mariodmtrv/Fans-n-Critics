from django.utils.six import _MovedItems
import datetime
__author__ = 'mario-dimitrov'
from django import template

register = template.Library()

from django.template.loader import get_template
from webapp.viewloaders.color_code_calc import generate_color_code
from webapp.movie_initialization import create_movie_data
from webapp.models import Movie

def generate_movie_data(movie_id):
    print("Movie Id" + movie_id)
    try:
        db_movie = Movie.objects.get(movie_id=movie_id)
        print('Movie exists')
    except:
        db_movie = create_movie_data(movie_id)
        print('Movie was created')
    class MovieData(Movie):
        def __init__(self, db_movie):
            db_movie = Movie.objects.get(movie_id=movie_id)
            if db_movie.description==None:
                self.description = "No description available"
            else:
                self.description = db_movie.description

            if db_movie.genres==None:
                self.genres = "No genres available"
            else:
                self.genres = db_movie.genres

            if db_movie.poster==None:
                self.poster = "No poster available"
            else:
                self.poster = db_movie.poster
            if db_movie.released == None:
                self.released = datetime.date(1900,1,1)
            else:
                self.released = db_movie.released
            self.title = db_movie.title
            self.overall_rating = 3.7
            self.color_code = generate_color_code(self.overall_rating)

    movie = MovieData(db_movie)
    return movie
