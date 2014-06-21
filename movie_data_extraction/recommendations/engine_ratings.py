from RatingEngine import RatingEngine
class EngineRatings():
    """
    Stores the movie ratings
    """
    __engines_data = {}
    def __init__(self, movie_name):
        pass
    def set_rating(self, engine):
        self.__engines_data[engine.engine_name]=engine.rating

