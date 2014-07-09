__author__ = 'mario-dimitrov'
from django import template

register = template.Library()

from django.template.loader import get_template
from webapp.models import Movie
from webapp.recommendations_generator import RecommendationsGenerator


def recommend(user):
    #generator = RecommendationsGenerator(user)
    """TODO"""
    class Result():
        image = '../static/images/men.jpg'
        title = "Two and a half"
        description = 'A well known sitcom'
        rating = '7.5'

    p = Result()
    rec_column_one = [p]
    rec_column_two = [p]
    rec_column_three = [p]
    return {'rec_column_one': rec_column_one, 'rec_column_two': rec_column_two, 'rec_column_three': rec_column_three}
