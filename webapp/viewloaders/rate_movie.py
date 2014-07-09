__author__ = 'mario-dimitrov'
from webapp.models import UserRatings
'''
Given the movie_id, username and rating from the form adds or changes the user rating
'''


def rate_the_movie(movie_id, username, rating):
    UserRatings.objects.filter(username=username, movie_id=movie_id).delete()
    p = UserRatings(movie_id=movie_id, username=username, rating=rating)
    p.save()
