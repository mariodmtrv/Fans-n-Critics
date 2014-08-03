from django.contrib import admin
from webapp.models import RatingEngine, Movie, UserRating, MovieReview, MovieGenre


class UserRatingAdmin(admin.ModelAdmin):
    fields = ['movie', 'rating', 'username']


class MovieAdmin(admin.ModelAdmin):
    fields = ['movie_id', 'description',
              'genres', 'poster', 'released', 'title']


class RatingEngineAdmin(admin.ModelAdmin):
    fields = ['rating', 'votes_count',
              'engine_name', 'engine_logo']


class MovieReviewAdmin(admin.ModelAdmin):
    fields = ['rating', 'link_address',
              'date']


class MovieGenreAdmin(admin.ModelAdmin):
    fields = ['genre_id', 'movie']


admin.site.register(RatingEngine, RatingEngineAdmin)
admin.site.register(MovieReview, MovieReviewAdmin)
admin.site.register(MovieGenre, MovieGenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(UserRating, UserRatingAdmin)
