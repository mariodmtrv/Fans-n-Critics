from webapp.models import Movie, MovieGenre
from engine.movie_finder.description_provider \
    import DescriptionProvider

__author__ = 'mario-dimitrov'


def create_movie_data(movie_id):
    d_provider = DescriptionProvider(movie_id)
    movie = Movie(movie_id=movie_id,
                  title=d_provider.get_name(),
                  description=d_provider.get_short_description(),
                  genres=d_provider.get_genre_list(),
                  poster=d_provider.get_poster_url(),
                  released=d_provider.get_released())
    movie.save()
    create_movie_genre_list(movie, d_provider.get_genre_list())
    return movie


def create_movie_genre_list(movie, string_genre_list):
    GENRES = {"Action": 1, "Adventure": 2, "Animation": 3, "Biography": 4,
              "Comedy": 5, "Crime": 6, "Documentary": 7,
              "Drama": 8, "Family": 9, "Fantasy": 10, "History": 11,
              "Horror": 12, "Music": 13, "Musical": 14, "Mystery": 15,
              "Romance": 16, "Sci-Fi": 17, "Sport": 18,
              "Thriller": 19, "War": 20, "Western": 21}

    for genre in string_genre_list:
        try:
            movie_genre_id = GENRES.get(genre)
            movie_genre_entry = MovieGenre(
                movie=movie, genre_id=movie_genre_id)
            movie_genre_entry.save()
        except:
            pass
