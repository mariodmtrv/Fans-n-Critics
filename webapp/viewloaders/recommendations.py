__author__ = 'mario-dimitrov'


class RecommendationTemplate():
    def __init__(self, image, title, description, rating):
        self.__image = image
        self.__title = title
        self.__description = description
        self.__rating = rating

    def get_image(self):
        return self.__image

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_rating(self):
        return self.__rating


def recommend(user):
    #generator = RecommendationsGenerator(user)
    """TODO"""

    p = RecommendationTemplate("image", "title", "description", "7.7")
    rec_column_one = [p]
    rec_column_two = [p]
    rec_column_three = [p]
    return {'rec_column_one': rec_column_one, 'rec_column_two': rec_column_two, 'rec_column_three': rec_column_three}
