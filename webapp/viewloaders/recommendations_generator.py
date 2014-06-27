__author__ = 'mario-dimitrov'
from webapp.models import Movie
from webapp.models import UserRatings

class RecommendationsGenerator():
    user_ratings = {}
    def __init__(self,user):
        movie = Movie.objects.filter(movie_id = "tt2278388")
        ratings = UserRatings.objects.filter(username = user)
        print(ratings)
        for rating in ratings:
            rated_movie = rating.movie_id
            self.add_movie_rating(rated_movie,ratings.rating)

    def add_movie_rating(self,rated_movie, rating):
        movie = Movie.objects.get(movie_id=rated_movie)
        genres = movie.genres
        for genre in genres:
            self.add_genre_data(genre,rating)


    def add_genre_data(self,genre, rating):
        current_genre_rating = self.user_ratings[genre]
        current_genre_rating[0] += rating
        current_genre_rating[1] += 1

    def calculate_genre_average(self):
        averaged_ratings = {}
        for genre, rating in self.user_ratings:
            averaged_ratings[genre] = rating[0]/rating[1]
        return averaged_ratings

    def generate_recommendations_list(self):
        result_list = []
        pass
