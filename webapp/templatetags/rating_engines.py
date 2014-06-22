__author__ = 'mario-dimitrov'
from django import template

register = template.Library()

from django.template.loader import get_template


def generate_rating_data(movie_id):
    """TODO"""

    class RatingEngineData():
        link_address = '../static/images/imdb-logo.png'
        votes = 1375
        rating = 7.5

    p = RatingEngineData()
    ratings = [p, p, p]
    return {'ratings': ratings}


t = get_template('rating_engines.html')
register.inclusion_tag(t)(generate_rating_data)