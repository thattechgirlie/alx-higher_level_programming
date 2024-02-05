#!/usr/bin/python3
"""Defines class and inherited function to check class."""


def is_kind_of_class(obj, a_class):
    """check if object is instance or inherited instance of class.
    Args:
        obj (any): Object to check.
        a_class (type): Class to match type of obj.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
