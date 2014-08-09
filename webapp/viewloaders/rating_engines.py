__author__ = 'mario-dimitrov'
from django import template

from engine.rating_engines.imdb_rating_engine import IMDBRatingEngine
from engine.rating_engines.rotten_tomato_rating_engine import RottenTomatoRatingEngine


register = template.Library()


class RatingEngineData():
    def __init__(self, engine):
        self.__rating = engine.rating()
        self.__link_address = engine.engine_logo()
        self.__votes = engine.votes_count()

    def get_rating(self):
        return self.__rating

    def get_link_address(self):
        return self.__link_address

    def get_votes(self):
        return self.__votes

    def set_link_address(self, address):
        self.__link_address = address

    def set_votes(self, votes):
        self.__votes = votes

    def set_rating(self, rating):
        self.__rating = rating


def generate_rating_data(movie_id):
    imdb = RatingEngineData(IMDBRatingEngine(movie_id))
    rotten_tomato = RatingEngineData(RottenTomatoRatingEngine(movie_id))
    ratings = [imdb, rotten_tomato]
    return ratings
