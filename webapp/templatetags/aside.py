__author__ = 'mario-dimitrov'
from django import template

register = template.Library()

from django.template.loader import get_template


def get_aside_content(aside_source):
    return {'aside_source': aside_source}


t = get_template('aside.html')
register.inclusion_tag(t)(get_aside_content)