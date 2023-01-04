#!/usr/bin/python3

"""
This is a module that adds two integers together
The modules must take two parameters a and b which must be integers
or floats
a and b must first be casted if they are floats
The module must return an integer: the addition of a and b
"""

def add_integer(a, b=98):
    """ 
    Returns the sum of two integers otherwise  raise a type error with the 
    message: a must be an integer or b must be an integer
    """
    h = list(map(lambda x: isinstance(x, (int, float)), [a, b]))

    if all(h):
        return int(a) + int(b)

    for x, y in list(zip(h, ['a', 'b'])):
        if not x:
            raise TypeError("{} must be an integer".format(y))
