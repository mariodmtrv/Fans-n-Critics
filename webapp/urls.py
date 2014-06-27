import webapp

__author__ = 'mario-dimitrov'
from webapp import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', 'webapp.views.search'),
    url(r'^login/$', 'webapp.views.login_view'),
    url(r'^logout/$', 'webapp.views.logout_view'),
    url(r'^movies/(\w){5,}/$', 'webapp.views.movie_info'),
    url(r'^rate/$','webapp.views.rate_movie'),
]

urlpatterns += staticfiles_urlpatterns()