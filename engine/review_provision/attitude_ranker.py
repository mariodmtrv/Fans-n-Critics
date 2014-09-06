__author__ = 'mario-dimitrov'
import os


class AttitudeRanker():
    """
    Calculates the rank of words based on dictionaries
    """
    POSITIVE = 1
    NEGATIVE = -1
    NOT_RATED = 0

    def __init__(self):
        files_relative_path = 'resources/dictionaries'
        dir = os.path.dirname(__file__)
        files_full_path = os.path.join(dir, files_relative_path)

        positive_file = os.path.join(files_full_path, 'positive-words.txt')
        self.__positives = AttitudeRanker.__read_attitude_file(
            positive_file)

        negative_file = os.path.join(files_full_path, 'negative-words.txt')
        self.__negatives = AttitudeRanker.__read_attitude_file(
            negative_file)

    @staticmethod
    def __read_attitude_file(file_path):
        with open(file_path, 'r') as attitude_file:
            file_data = attitude_file.read().split()
            result_set = set(file_data)
            return result_set

    def categorize_word(self, word):
        """
        Due to a limited dictionary of words only ranks of positive, negative and not available are in present
        """
        if word in self.__positives:
            return self.POSITIVE
        elif word in self.__negatives:
            return self.NEGATIVE
        else:
            return self.NOT_RATED
