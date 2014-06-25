from django.utils.six import _MovedItems

__author__ = 'mario-dimitrov'
from django import template

register = template.Library()

from django.template.loader import get_template
from webapp.templatetags.color_code_calc import generate_color_code
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
            if len(db_movie.description)==0:
                self.description = "No description available"
            else:
                self.description = db_movie.description

            if len(db_movie.genres)==0:
                self.genres = "No genres available"
            else:
                self.genres = db_movie.genres

            if len(db_movie.poster)==0:
                self.poster = "No poster available"
            else:
                self.poster = db_movie.poster
            self.released = db_movie.released
            self.title = db_movie.title
            self.overall_rating = 3.7
            self.color_code = generate_color_code(self.overall_rating)

    movie = MovieData(db_movie)
    return {'movie': movie}


t = get_template('movie_data.html')
register.inclusion_tag(t)(generate_movie_data)
