__author__ = 'mario-dimitrov'
from django import template

from webapp.models import Movie

register = template.Library()

from webapp.template_classes.movie_initialization import create_movie_data
from webapp.template_classes.movie_data import MovieData


def generate_movie_data(movie_id):
    try:
        db_movie = Movie.objects.get(movie_id=movie_id)
    except:
        db_movie = create_movie_data(movie_id)
    movie = MovieData(db_movie)
    return movie
