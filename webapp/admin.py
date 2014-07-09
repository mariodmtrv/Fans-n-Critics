from django.contrib import admin
from webapp.models import RatingEngine, Movie, UserRatings, MovieReview


class UserRatingsAdmin(admin.ModelAdmin):
    fields = ['movie_id', 'rating', 'username']


class MovieAdmin(admin.ModelAdmin):
    fields = ['movie_id', 'description',
              'genres', 'poster', 'released', 'title']

admin.site.register(Movie, MovieAdmin)
admin.site.register(UserRatings, UserRatingsAdmin)
