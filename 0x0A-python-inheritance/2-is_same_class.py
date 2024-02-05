#!/usr/bin/python3
"""Define a function to check class."""


def is_same_class(obj, a_class):
    """Check if object is instance of class.
    Args:
        obj (any): Object to check.
        a_class (type): Class to match type of obj.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
