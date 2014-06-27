import re

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from movie_data_extraction.movie_finder.movie_search import MovieSearch
from webapp.viewloaders.rate_movie import rate_the_movie
from webapp.viewloaders.movie_data import generate_movie_data
from webapp.viewloaders.rating_engines import generate_rating_data
from webapp.viewloaders.review_table import generate_review_table
from webapp.viewloaders.recommendations import recommend

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        recommendations = recommend(request.user.username)
        return render_to_response('base.html',{"rec_column_one":recommendations.get("rec_column_one"),"rec_column_two":recommendations.get("rec_column_two"), "rec_column_three":recommendations.get("rec_column_three")}, context_instance=RequestContext(request))
    else:
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

def rate_movie(request):
    print("Form accepted")
    if request.user.is_authenticated():
        username = request.user.username
    rating = request.GET['rating']
    movie_id = request.GET['movie_id']
    print("User voted" + rating + "    " +  movie_id + "    " + username)
    rate_the_movie(movie_id,username,rating)


def movie_info(request, movie_id):
    ''''hotel = get_object_or_404(Hotel, id=hotel_id)
    photo_album = Photo.objects.filter(hotel=hotel_id)'''
    regex = re.compile('\w+/$')
    movie_res_id = (regex.findall(request.path)[0][:-1])
    movie_data = generate_movie_data(movie_res_id)
    ratings = generate_rating_data(movie_res_id)
    ratings_table =generate_review_table(movie_res_id)
    print(movie_res_id)
    return render_to_response("movie-article.html", {"movie_id": movie_res_id, "movie" : movie_data, "ratings": ratings, "ratings_table":ratings_table },
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
            return HttpResponse('<h1>You enter the wrong neighbourhood stalker flower</h1>', status=401)
    '''return render_to_response('base.html', context_instance=RequestContext(request))'''


def logout_view(request):
    logout(request)
    return render_to_response('base.html', context_instance=RequestContext(request))