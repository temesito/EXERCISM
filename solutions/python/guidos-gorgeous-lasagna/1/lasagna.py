"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(already_bake_time):
    """C
    """
    return  EXPECTED_BAKE_TIME - already_bake_time
def preparation_time_in_minutes(number_layers):
    """C
    """
    return number_layers * PREPARATION_TIME
def elapsed_time_in_minutes(number_layers, elapsed_bake_time):
    """f
    """
    return preparation_time_in_minutes(number_layers) + elapsed_bake_time
