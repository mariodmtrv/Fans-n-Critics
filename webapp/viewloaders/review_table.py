__author__ = 'mario-dimitrov'
from django import template

from engine.review_provision.review_crawler import ReviewCrawler


register = template.Library()
from webapp.viewloaders.color_code_calc import generate_color_code
from engine.review_provision.review_ranker import ReviewRanker
from engine.review_provision.review_parser import ReviewParser


class MovieReview():
    def __init__(self, link_address, date, rating, index):
        self.link_address = link_address
        self.date = date
        self.rating = rating
        self.color_code = generate_color_code(rating)
        self.index = index


def generate_review_table(movie_data):
    crawler = ReviewCrawler()
    crawler.search_query(movie_data.title)
    print(crawler.get_results_count())
    ratings_table = []
    reviews_count = crawler.get_results_count()
    actual_review_index = 1
    for review_index in range(0, reviews_count):
        review_url = crawler.get_result_url(review_index)
        try:
            parser = ReviewParser()
            page_html = parser.extract_page(review_url)
            review_date = parser.get_result_date(review_index)
            review_data = parser.extract_review_words(page_html)
            ranker = ReviewRanker(review_data)
            review_rating = ranker.calculate_review_rank()
            actual_review_index += 1
            rating_entity = MovieReview(review_url, review_date, review_rating, actual_review_index)
            ratings_table.append(rating_entity)
        except:
            pass
    return ratings_table
