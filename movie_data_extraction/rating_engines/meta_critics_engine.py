from RatingEngine import RatingEngine
import metacritics

'''
class MetaCriticsEngine(RatingEngine):
    """Represents the IMDB rating engine and its results for a movie"""
    def __init__(self, movie_name):
        scraper = metacritics.Scraper()
        movie_url = "http://www.metacritic.com/movie/"+('-').join(str(movie_name).split(' '))
        resource = scraper.get(movie_url)
        self.__movie_name = movie_name
        self.__rating = resource.metascore
        self.__votes = ""
        self.__name = "MetaCritics"
        self.__logo = "resources/logos/MetaCritics"
    def rating(self):
        return self.__rating
    def engine_logo(self):
        return self.__logo
    def engine_name(self):
        return self.__name
    def votes_count(self):
        return self.__votes
        '''
