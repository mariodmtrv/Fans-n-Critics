from django.shortcuts import render, loader
from django.shortcuts import render_to_response
from django.template import Context
from django.http import HttpResponse
from movie_data_extraction.movie_finder.description_provider import DescriptionProvider
from movie_data_extraction.movie_finder.movie_search import MovieSearch
# Create your views here.

def index(request):
    return render_to_response('index.html')


'''
Performs the movie query search
and repacks the result for the template
'''


def search(movie_name):
    query = movie_name.GET['q']
    searcher = MovieSearch()
    alternatives = searcher.get_alternatives_list(query, 5)
    alternatives_result = []

    class Alternatives():
        def __init__(self, alt):
            self.title = alt.get('title')
            self.year = alt.get('year')

    for movie in alternatives:
        res = Alternatives(movie)
        alternatives_result.append(res)

    t = loader.get_template('index.html')
    c = Context({'alternatives': alternatives_result})
    return HttpResponse(t.render(c))