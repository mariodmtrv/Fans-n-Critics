__author__ = 'mario-dimitrov'
from engine.recommendations.recommendations_generator import RecommendationsGenerator
from webapp.template_classes.movie_data import URL
from webapp.models import Movie


class RecommendationTemplate():
    def __init__(self, image, title, description, rating, href):
        self.__image = image
        self.__title = title
        self.__description = description
        self.__rating = rating
        self.__href = href

    def get_image(self):
        return self.__image

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_rating(self):
        return self.__rating

    def get_href(self):
        return self.__href


class RecommendationsAdapter(RecommendationTemplate):
    def __init__(self, movie):
        movie_rating = 7.5
        print(movie.title)
        image_url = movie.title + movie.released.strftime('%m%d%Y') + ".jpg"
        RecommendationTemplate.__init__(self, URL + image_url,
                                        movie.title, movie.description[:50] + "...",
                                        movie_rating, movie.movie_id)


def recommend(user):
    movies = Movie.objects.all()[:10]
    generator = RecommendationsGenerator(user, movies)
    entities = generator.get_recommendations()
    viewable_results = []
    for entity in entities:
        viewable_results.append(RecommendationsAdapter(entity))
    rec_column_one = viewable_results[:2]
    rec_column_two = viewable_results[2:4]
    rec_column_three = viewable_results[4:6]
    return {'rec_column_one': rec_column_one,
            'rec_column_two': rec_column_two, 'rec_column_three': rec_column_three}
