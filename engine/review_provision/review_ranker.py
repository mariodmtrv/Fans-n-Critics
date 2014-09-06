from engine.review_provision.attitude_ranker import AttitudeRanker

__author__ = 'mario-dimitrov'
import math


class ReviewRanker():
    __LOG_BASE = 1.25

    def __init__(self, words_list):
        self.__words_list = words_list

    def __calculate_word_ranks(self):
        ranker = AttitudeRanker()
        ranks = [ranker.categorize_word(word)
                 for word in self.__words_list]
        self.__positive_count = len(
            [rank for rank in ranks if rank == AttitudeRanker.POSITIVE])
        self.__negative_count = len(
            [rank for rank in ranks if rank == AttitudeRanker.NEGATIVE])

    def calculate_review_rank(self):
        self.__calculate_word_ranks()
        rank = 5.0 + \
               math.log(
                   self.__positive_count / self.__negative_count,
                   self.__LOG_BASE)
        rank = min(rank, 10.0)
        rank = max(rank, 1.0)

        return math.floor(rank * 10.0 + 0.5) / 10.0
