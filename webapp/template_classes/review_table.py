__author__ = 'mario-dimitrov'
from datetime import datetime

from django import template

from engine.review_provision.review_crawler import ReviewCrawler

register = template.Library()
from webapp.viewloaders.color_code_calc import generate_color_code
from engine.review_provision.review_ranker import ReviewRanker
from engine.review_provision.review_parser import ReviewParser
from webapp.models import MovieReview, Movie


class MovieReviewView():
    def __init__(self, link_address, date, rating, index):
        self.link_address = link_address
        self.date = date
        self.rating = rating
        self.color_code = generate_color_code(rating)
        self.index = index


def generate_review_table(movie_res_id):
    ratings_table = []
    movie_data = Movie.objects.get(movie_id=movie_res_id)
    try:
        reviews = MovieReview.objects.all().filter(movie=movie_data)
    except:
        # No data is available, try to obtain some
        obtain_review_data(movie_data)
        try:
            reviews = MovieReview.objects.get(movie=movie_data)
        except:
            # Still no data, pity
            return ratings_table
    review_id = 0
    for review_data in reviews:
        review_id += 1
        rating_entity = MovieReviewView(
            review_data.link_address,
            review_data.date, review_data.rating, review_id)
        ratings_table.append(rating_entity)
    return ratings_table


def obtain_review_data(movie_data):
    crawler = ReviewCrawler()
    #try:
    crawler.search_query(movie_data.title)
    reviews_count = crawler.get_results_count()
    actual_review_index = 0
    for review_index in range(0, reviews_count):
        #try:
        review_url = crawler.get_result_url(review_index)
        parser = ReviewParser()
        page_html = parser.extract_page(review_url)
        review_date = parser.get_result_date()
        review_data = parser.extract_review_words(page_html)
        ranker = ReviewRanker(review_data)
        review_rating = ranker.calculate_review_rank()
        actual_review_index += 1
        rating_entity = MovieReview(movie=movie_data,
                                    link_address=review_url,
                                    date=datetime.now(),
                                    rating=review_rating)
        rating_entity.save()
        if actual_review_index >= 5:
            break
            # except:
            # traceback.print_exc(file=sys.stdout)
            # pass
            # except:
            # traceback.print_exc(file=sys.stdout)
            # pass
