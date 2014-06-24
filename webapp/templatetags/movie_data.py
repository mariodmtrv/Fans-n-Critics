from django.utils.six import _MovedItems

__author__ = 'mario-dimitrov'
from django import template

register = template.Library()

from django.template.loader import get_template
from webapp.templatetags.color_code_calc import generate_color_code


def generate_movie_data(movie_id):
    """TODO"""
    class MovieData():
        poster = "../static/images/monty.jpg"
        title = "Monty Python and the Holy Grail"
        released = '15-May-1979'
        summary = "A theatrical re-release of the 1975 Python classic" + \
                  "with a new print, additional footage, and remastered soundtrack."
        starring = 'Eric Idle, Graham Chapman, John Cleese, Michael Palin, Terry Gilliam, Terry Jones'
        overall_rating = 8.5
        color_code = generate_color_code(overall_rating)

    movie = MovieData()
    return {'movie': movie}


t = get_template('movie_data.html')
register.inclusion_tag(t)(generate_movie_data)
