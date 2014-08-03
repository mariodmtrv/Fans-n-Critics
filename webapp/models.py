from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Movie(models.Model):
    movie_id = models.CharField(max_length=25, unique=True)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=250)
    photo_path = "/images/"
    genres = models.CharField(max_length=200)
    poster = models.CharField(max_length=100)
    released = models.DateField()


class RatingEngine(models.Model):
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    votes_count = models.IntegerField(validators=[MinValueValidator(1)])
    engine_name = models.CharField(max_length=25)
    engine_logo = models.CharField(max_length=80)
    movie = models.ForeignKey(Movie)


class MovieReview(models.Model):
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    link_address = models.CharField(max_length=80)
    date = models.DateField()
    movie = models.ForeignKey(Movie)


class MovieGenre(models.Model):
    genre_id = models.IntegerField()
    movie = models.ForeignKey(Movie)


class UserRating(models.Model):
    username = models.CharField(max_length=25)
    movie = models.ForeignKey(Movie)
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
