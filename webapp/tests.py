import urllib.request
import shutil
from django.test import TestCase

from webapp.viewloaders.color_code_calc import generate_color_code
from webapp.recommendations_generator import RecommendationsGenerator


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
        print(x)


class ImgTests(TestCase):
    def test_urls(self):
        url = "http://ia.media-imdb.com/" \
              "images/M/MV5BMTQwNjU5MzUzNl5BMl5BanBnXkFtZTYwMzc1MTI3._V1_SY317_CR0,0,214,317_AL_.jpg"

        with urllib.request.urlopen(url) as response, open("resultfile.jpg", 'wb') as out_file:
            shutil.copyfileobj(response, out_file)