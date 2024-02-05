#!/usr/bin/python3
"""Defines function to check class."""


def inherits_from(obj, a_class):
    """Check if object is inherited instance of class.
    Args:
        obj (any): Object to check.
        a_class (type): Class to match type of obj.
    Returns:
        If obj is inherited instance if a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
