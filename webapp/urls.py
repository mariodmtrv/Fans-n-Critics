__author__ = 'mario-dimitrov'
from webapp import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', 'webapp.views.search'),
]