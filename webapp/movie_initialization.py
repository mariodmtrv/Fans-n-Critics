from webapp.models import Movie
import datetime
from movie_data_extraction.movie_finder.description_provider import DescriptionProvider
__author__ = 'mario-dimitrov'

def create_movie_data(movie_id):
    '''d_provider = DescriptionProvider(movie_id)
    p = Movie(movie_id=movie_id,title = d_provider.get_name(),
              description = d_provider.get_short_description(),
              genres = d_provider.get_genre_list(),
              poster = d_provider.get_poster_url(),
              released = d_provider.get_released())'''
    p = Movie(movie_id="dasdas",title = "dasdasd",
              description = "dasdasd",
              genres = "dasdasd",
              poster = "dasdasdasd",
              released = datetime.date(1975,5,25))
    p.save()
    '''Load more data here'''

create_movie_data("tt0071853")