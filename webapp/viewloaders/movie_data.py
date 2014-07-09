from django.utils.six import _MovedItems
import datetime
__author__ = 'mario-dimitrov'
from django import template
from webapp.models import Movie
register = template.Library()

from django.template.loader import get_template

from webapp.movie_initialization import create_movie_data
from webapp.template_classes.movie_data import MovieData

def generate_movie_data(movie_id):
    print("Movie Id" + movie_id)
    try:
        db_movie = Movie.objects.get(movie_id=movie_id)
        print('Movie exists')
    except:
        db_movie = create_movie_data(movie_id)
        print('Movie was created')
    movie = MovieData(db_movie)
    return movie
