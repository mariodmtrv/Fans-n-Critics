from http.cookiejar import user_domain_match
from django.shortcuts import render, loader
from django.shortcuts import render_to_response
from django.template import RequestContext, Context

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from movie_data_extraction.movie_finder.description_provider import DescriptionProvider
from movie_data_extraction.movie_finder.movie_search import MovieSearch
import re
# Create your views here.
def index(request):
    return render_to_response('base.html', context_instance=RequestContext(request))


'''
Performs the movie query search
and repacks the result for the template
'''


def search(request):
    query = request.GET['q']
    searcher = MovieSearch()
    alternatives = searcher.get_alternatives_list(query, 5)
    alternatives_result = []

    class Alternatives():
        def __init__(self, alt):
            self.title = alt.get('title')
            self.year = alt.get('year')
            self.movie_id = alt.get('imdb_id')

    for movie in alternatives:
        res = Alternatives(movie)
        alternatives_result.append(res)
    return render_to_response('base.html', {'alternatives': alternatives_result},
                              context_instance=RequestContext(request))


def movie_info(request, movie_id):
    ''''hotel = get_object_or_404(Hotel, id=hotel_id)
    photo_album = Photo.objects.filter(hotel=hotel_id)'''
    regex = re.compile('\w+/$')
    movie_res_id = (regex.findall(request.path)[0][:-1])
    print(movie_res_id)
    return render_to_response("movie-article.html", {"movie_id": movie_res_id},
                              context_instance=RequestContext(request))


@csrf_protect
def login_view(request):
    login_data = request.POST if request.POST else None
    if request.method == 'POST':
        username = request.POST.get('username', '')
        user = authenticate(username=request.POST.get('username', ''), password=request.POST.get('password', ''))
        if user is not None:
            login(request, user)
            return render_to_response('base.html', context_instance=RequestContext(request))
        else:
            print(username)
            return HttpResponse('<h1>User authentication failed</h1>', status=401)
    '''return render_to_response('base.html', context_instance=RequestContext(request))'''


def logout_view(request):
    logout(request)
    return render_to_response('base.html', context_instance=RequestContext(request))