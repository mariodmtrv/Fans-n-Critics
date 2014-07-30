__author__ = 'mario-dimitrov'
from django import template
from movie_data_extraction.review_provision.review_crawler import ReviewCrawler

register = template.Library()
from django.template.loader import get_template
from webapp.viewloaders.color_code_calc import generate_color_code


class MovieReview():
    def __init__(self, link_address, date, rating, index):
        self.link_address = link_address
        self.date = date
        self.rating = rating
        self.color_code = generate_color_code(rating)
        self.index = index + 1


def generate_review_table(movie_title):
    crawler = ReviewCrawler()
    crawler.search_query(movie_title)
    print(crawler.get_results_count())
    ratings_table = []
    reviews_count = min(5, crawler.get_results_count())
    for review_index in range(0, reviews_count):
        review_url = crawler.get_result_url(review_index)
        review_date = crawler.get_result_date(review_index)
        ### TODO run an actual rating calculator here
        review_rating = 7.5
        rating_entity = MovieReview(review_url, review_date, review_rating, review_index)
        ratings_table.append(rating_entity)
    return ratings_table
