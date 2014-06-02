class DistanceCalculator():
    def __init__(self):
        pass
    def calculate_distance(self, current_movie, other_movie,  user_genre_ratings):
        distance = 0;
        other_movie = []
        for genre_index in range(len(current_movie)):
            value = (current_movie[genre_index] -other_movie[genre_index])*user_genre_ratings
