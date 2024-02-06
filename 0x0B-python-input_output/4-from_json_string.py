#!/usr/bin/python3
# 6-from_json_string.py
"""Define JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return python object representation of JSON string."""
    return json.loads(my_str)
