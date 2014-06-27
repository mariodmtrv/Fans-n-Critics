__author__ = 'mario-dimitrov'
from webapp.models import UserRatings
def rate_movie(movie_id,username, rating):
    p = UserRatings(movie_id=movie_id)
    p.save()