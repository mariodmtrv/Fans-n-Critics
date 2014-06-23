from http.cookiejar import user_domain_match
from django.shortcuts import render, loader
from django.shortcuts import render_to_response
from django.template import RequestContext,Context

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from movie_data_extraction.movie_finder.description_provider import DescriptionProvider
from movie_data_extraction.movie_finder.movie_search import MovieSearch
# Create your views here.
def index(request):
    return render_to_response('index.html',context_instance=RequestContext(request))


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

@csrf_protect
def login_view(request):
    login_data = request.POST if request.POST else None
    if request.method == 'POST':
        username=request.POST.get('username', '')
        user = authenticate(username=request.POST.get('username', ''), password=request.POST.get('password', ''))
        if user is not None:
            login(request, user)
            return render_to_response('logged.html', {'username': username}, context_instance=RequestContext(request))
            return HttpResponseRedirect('/logged.html/')
        else:
            print(username)
            return HttpResponse('<h1>Failed</h1>',status = 401)
    return render_to_response('index.html', context_instance=RequestContext(request))