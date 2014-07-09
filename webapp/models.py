from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Movie(models.Model):
    movie_id = models.CharField(max_length=25)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=250)
    genres = models.CharField(max_length=300)
    poster = models.CharField(max_length=80)
    released = models.DateField()


class RatingEngine(models.Model):
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    votes_count = models.IntegerField(validators=[MinValueValidator(1)])
    engine_name = models.CharField(max_length=25)
    engine_logo = models.CharField(max_length=80)
    movie_id = models.ForeignKey(Movie)


class MovieReview(models.Model):
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    link_address = models.CharField(max_length=80)
    date = models.DateField()
    movie_id = models.ForeignKey(Movie)


class UserRatings(models.Model):
    username = models.CharField(max_length=25)
    movie_id = models.ManyToManyField(Movie)
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
