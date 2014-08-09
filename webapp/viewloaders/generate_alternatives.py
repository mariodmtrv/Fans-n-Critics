__author__ = 'mario-dimitrov'

from engine.movie_finder.movie_search import MovieSearch


class Alternatives():
    def __init__(self, alt):
        self.title = alt.get('title')
        self.year = alt.get('year')
        self.movie_id = alt.get('imdb_id')

    @staticmethod
    def generate_alternatives(query):
        searcher = MovieSearch()
        alternatives = searcher.get_alternatives_list(query, 5)
        alternatives_result = []
        for movie in alternatives:
            res = Alternatives(movie)
            alternatives_result.append(res)
        return alternatives_result
