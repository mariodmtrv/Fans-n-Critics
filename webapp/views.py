import re

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from webapp.viewloaders.rate_movie import rate_the_movie
from webapp.viewloaders.movie_data import generate_movie_data
from webapp.viewloaders.rating_engines import generate_rating_data
from webapp.viewloaders.review_table import generate_review_table
from webapp.viewloaders.generate_alternatives import generate_alternatives
from webapp.viewloaders.generate_recommendations_list import generate_list


def index(request):
    if request.user.is_authenticated():
        recommendations = generate_list(request.user.username)
        return render_to_response('base.html',
                                  recommendations, context_instance=RequestContext(request))
    else:
        return render_to_response('base.html', context_instance=RequestContext(request))


'''
Performs the movie query search
and repacks the result for the template
'''


def search(request):
    query = request.GET['q']
    alternatives_result = generate_alternatives(query)
    return render_to_response('base.html', {'alternatives': alternatives_result},
                              context_instance=RequestContext(request))


def register(request):
    first_name = request.POST.get('first_name')
    username = request.POST.get('username')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password_confirmation = request.POST.get('password_confirmation')
    if password == password_confirmation:
        count = User.objects.filter(username=username).count()
        if count > 0:
            return render_to_response('base.html',
                                      {"should_show_message": "true",
                                       "message_header": "Failed", "message_content": "This username exists"},
                                      context_instance=RequestContext(request))
        else:
            user = User()
            user.password = password
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()
            return render_to_response('base.html',
                                      {"should_show_message": "true", "message_header": "Created user " + username,
                                       "message_content": "Your account has been confirmed. Now you may login."},
                                      context_instance=RequestContext(request))
    return render_to_response('base.html', context_instance=RequestContext(request))


def rate_movie(request):
    print("Form accepted")
    if request.user.is_authenticated():
        username = request.user.username
    rating = request.GET['rating']
    movie_id = request.GET['movie_id']
    print("User voted" + rating + "    " + movie_id + "    " + username)
    rate_the_movie(
        movie_id, username, rating, context_instance=RequestContext(request))


def movie_info(request, id):
    regex = re.compile('\w+/$')
    movie_res_id = (regex.findall(request.path)[0][:-1])
    movie_data = generate_movie_data(movie_res_id)
    ratings = generate_rating_data(movie_res_id)
    ratings_table = generate_review_table(movie_res_id)
    print(movie_res_id)
    return render_to_response("movie-article.html",
                              {"movie_id": movie_res_id, "movie": movie_data,
                               "ratings": ratings, "ratings_table": ratings_table},
                              context_instance=RequestContext(request))


@csrf_protect
def login_view(request):
    login_data = request.POST if request.POST else None
    if request.method == 'POST':
        username = request.POST.get('username', '')
        user = authenticate(username=request.POST.get(
            'username', ''), password=request.POST.get('password', ''))
        if user is not None:
            login(request, user)
            recommendations = generate_list(user)
            success_log = {"should_show_message": "true",
                           "message_header": "Welcome",
                           "message_content": "Oh, yeah, welcome " + username,
            }

            return render_to_response('base.html', dict(list(recommendations.items()) + list(success_log.items())),
                                      context_instance=RequestContext(request))
        else:
            return render_to_response('base.html',
                                      {"should_show_message": "true", "message_header": "Failed",
                                       "message_content": "Authentication failed for user " + username +
                                                          ". Please check your data and try again"},
                                      context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return render_to_response('base.html', context_instance=RequestContext(request))
