__author__ = 'mario-dimitrov'
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from webapp import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', 'webapp.views.register'),
    url(r'^search/$', 'webapp.views.search'),
    url(r'^login/$', 'webapp.views.login_view'),
    url(r'^logout/$', 'webapp.views.logout_view'),
    url(r'^movies/(\w){5,}/$', 'webapp.views.movie_info'),
    url(r'^rate_movie/$', 'webapp.views.rate_movie'),
]
urlpatterns += staticfiles_urlpatterns()
