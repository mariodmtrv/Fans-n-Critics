__author__ = 'mario-dimitrov'
from django import template

register = template.Library()


def generate_rating_data(movie_id):
    """TODO"""
    #engineData = RatingEngine.objects.get(movie_id=movie_id)
    class RatingEngineData():
        link_address = ''
        votes = 1375
        rating = 7.5

    p = RatingEngineData()
    p.link_address = "http://www.cinephreakpictures.com/images/imdb_logo_small.png"
    q = RatingEngineData()
    q.rating = 6.8
    q.votes = 1115
    q.link_address = "http://www.userlogos.org/files/logos/jumpordie/rottentomatoes_03.png"

    ratings = [p, q]
    return ratings
