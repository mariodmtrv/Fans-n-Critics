__author__ = 'mario-dimitrov'
from webapp.models import UserRating, Movie

'''
Given the movie_id, username and rating from the form adds or changes the user rating
'''


def rate_the_movie(movie_id_str, username, rating):
    movies = Movie.objects.filter(movie_id=movie_id_str)
    movie_instance = list(movies)[0]
    print(movie_instance.title)
    if movie_instance:
        p = UserRating(
            username=username, movie=movie_instance, rating=rating)
        p.save()
