__author__ = 'mario-dimitrov'
from django import template
register = template.Library()

from django.template.loader import get_template
from webapp.templatetags.color_code_calc import generate_color_code


def generate_review_table(movie_id):
    """TODO"""

    class MovieReview():
        link_address = 'http://google.com'
        date = '15-May-2014'
        rating = 7.5
        color_code = generate_color_code(rating)


    p = MovieReview()
    ratings = [p, p, p, p, p, p]
    return {'ratings': ratings}


t = get_template('review_table.html')
register.inclusion_tag(t)(generate_review_table)