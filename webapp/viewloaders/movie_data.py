__author__ = 'mario-dimitrov'
from django import template

from webapp.models import Movie
from webapp.viewloaders.rating_engines import generate_rating_data
from webapp.template_classes.review_table import generate_review_table

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


def generate_all_movie_parameters(movie_res_id):
    movie_data = generate_movie_data(movie_res_id)
    ratings = generate_rating_data(movie_res_id)
    ratings_table = generate_review_table(movie_res_id)
    parameters = {"movie_id": movie_res_id, "movie": movie_data,
                  "ratings": ratings, "ratings_table": ratings_table}
    return parameters
