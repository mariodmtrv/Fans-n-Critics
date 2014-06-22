__author__ = 'mario-dimitrov'
from django import template

register = template.Library()

from django.template.loader import get_template


def recommend(user):
    """TODO"""

    class Result():
        image = '../static/images/men.jpg'
        title = 'Two and a half men'
        description = 'Sucks a lot ...'
        rating = '7.5'

    p = Result()
    rec_column_one = [p, p]
    rec_column_two = [p, p]
    rec_column_three = [p, p]
    return {'rec_column_one': rec_column_one, 'rec_column_two': rec_column_two, 'rec_column_three': rec_column_three}


t = get_template('recommendations.html')
register.inclusion_tag(t)(recommend)