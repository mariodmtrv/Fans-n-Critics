__author__ = 'mario-dimitrov'
from webapp.models import Movie
from webapp.models import UserRating


class RecommendationsGenerator():
    user_ratings = {}

    def __init__(self, user, movies):
        self.user = user
        self.movies = movies

    def calculate_ratings(self):
        ratings = UserRating.objects.filter(username=self.user)
        print(ratings)

        for rating in ratings:
            rated_movie = rating.movie_id
            user_rating = 0
            self.add_movie_rating(rated_movie, user_rating)

    def add_movie_rating(self, rated_movie, rating):
        movie = Movie.objects.get(movie_id=rated_movie)
        genres = movie.genres
        for genre in genres:
            self.add_genre_data(genre, rating)

    def add_genre_data(self, genre, rating):
        current_genre_rating = self.user_ratings[genre]
        current_genre_rating[0] += rating
        current_genre_rating[1] += 1

    def calculate_genre_average(self):
        averaged_ratings = {}
        for genre, rating in self.user_ratings:
            averaged_ratings[genre] = rating[0] / rating[1]
        return averaged_ratings

    def generate_recommendations_list(self):
        user_ratings_average = self.calculate_genre_average()
        movies = Movie.objects.all()
        for movie in movies:
            rating_difference = 0
            genres_count = 0
            for genre in movie.genres:
                if genre in user_ratings_average.keys():
                    rating_difference += user_ratings_average[genre]

    def get_recommendations(self):
        return self.movies[:6]
