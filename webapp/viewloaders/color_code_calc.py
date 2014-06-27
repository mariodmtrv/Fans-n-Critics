__author__ = 'mario-dimitrov'

'''
Generates the color code types for the bootstrap coloring scheme
'''


def generate_color_code(rating):
    # Use a dict here?
    color_codes = ["success", "warning", "danger"]
    border_rating_low = 4.0
    border_rating_medium = 6.5
    color_code = color_codes[0]
    if ( rating < border_rating_medium):
        color_code = color_codes[1]
    if ( rating < border_rating_low):
        color_code = color_codes[2]
    return color_code