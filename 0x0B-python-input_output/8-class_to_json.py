#!/usr/bin/python3
"""Define python class-to-JSON function."""


def class_to_json(obj):
    """Return dictionary representation of simple data structure."""
    return obj.__dict__
