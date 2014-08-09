__author__ = 'mario-dimitrov'
from webapp.models import RatingEngine
from webapp.models import MovieReview


class OverallRatingGenerator():
    def __init__(self, movie_id):
        self.rating_engines = RatingEngine.objects.filter(movie_id=movie_id)
        self.reviews = MovieReview.objects.filter(movie_id=movie_id)

    def calculate_engine_rating(self):
        total_rating = 0
        votes_count = 0
        for engine in self.rating_engines:
            if engine.votes_count > 0:
                total_rating += engine.rating * engine.votes_count
                votes_count += engine.votes_count
        return total_rating / votes_count

    def calculate_review_rating(self):
        total_ratings = 0
        for review in self.reviews:
            total_ratings += review.rating
        return total_ratings / len(self.reviews)

    def calculate_movie_rating(self):
        engine_rating = self.calculate_engine_rating()
        review_rating = self.calculate_review_rating()
        engine_ratio = 0.75
        review_ratio = 0.25
        if len(self.reviews) == 0:
            engine_ratio = 1
            review_ratio = 0
        if (len(self.reviews) > 6):
            engine_ratio = 0.65
            review_ratio = 0.35
        return engine_rating * engine_ratio + review_rating * review_ratio
