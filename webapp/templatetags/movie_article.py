__author__ = 'mario-dimitrov'
from django import template

register = template.Library()

from django.template.loader import get_template


def generate_movie_article(movie_id):
    return {'res': ''}


t = get_template('movie_article.html')
register.inclusion_tag(t)(generate_movie_article)