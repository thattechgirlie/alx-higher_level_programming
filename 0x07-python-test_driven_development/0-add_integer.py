#!/usr/bin/python3
"""Function to add integers."""


def add_integer(a, b=98):
    """Gives us addition of a and b.
    
    Typecast float arguments to integers before performing addition.

    Raises:
        TypeError:If either a or b is a non integer or non float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
