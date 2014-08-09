__author__ = 'mario-dimitrov'
from webapp.viewloaders.recommendations import recommend

def generate_list(username):
    recommendations = recommend(username)
    recommendations_list = {"rec_column_one": recommendations.get("rec_column_one"),
                            "rec_column_two": recommendations.get("rec_column_two"),
                            "rec_column_three": recommendations.get("rec_column_three")}
    return recommendations_list