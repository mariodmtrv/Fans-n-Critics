from django.db.models.sql.datastructures import Date
from django.test import TestCase
from movie_data_extraction.rating_engines import rating_engine

from webapp.viewloaders.color_code_calc import generate_color_code
from recommendations.recommendations_generator import RecommendationsGenerator
from webapp.models import UserRatings, Movie


class ColorCodingTest(TestCase):
    def test_color_code_large_number(self):
        actual = generate_color_code(100.32)
        expected = "success"
        self.assertEqual(actual, expected)

    def test_color_code_borderline(self):
        actual = generate_color_code(6.499999999)
        expected = "warning"
        self.assertEqual(actual, expected)


class RecommendationsTest(TestCase):
    def test_user_genre_ratings(self):
        generator = RecommendationsGenerator("user")
        x = generator.calculate_genre_average()