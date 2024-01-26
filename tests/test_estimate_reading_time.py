from lib.estimate_reading_time import *
from sample_texts import *


# if the string is less than 200 words, return 'less than a minute' for the estimated reading time.
def test_short_text():
    estimated_time = estimate_reading_time('I am a tiny little sentence.')
    assert estimated_time == 'Estimated reading time: less than a minute.'

# if the string is empty, return 'please provide a text'

def test_empty_text():
    estimated_time = estimate_reading_time('')
    assert estimated_time == 'Please provide a text.'

# if the string is between 200 (1 minute) and 12,000 (60 minutes) words long, return reading time in minutes

def test_sub_hour_text():
    estimated_time = estimate_reading_time(herbert_west)
    assert estimated_time == 'Estimated reading time: 59 minutes.'

# if string is >= 12,000 words, return estimated reading time in hours and minutes

def test_over_hour_text():
    estimated_time = estimate_reading_time(at_the_mountains_of_madness)
    assert estimated_time == 'Estimated reading time: 3 hours and 22 minutes.'