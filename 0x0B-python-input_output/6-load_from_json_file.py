#!/usr/bin/python3
"""Define function to read JSON file."""
import json


def load_from_json_file(filename):
    """Create python object from JSON file."""
    with open(filename) as f:
        return json.load(f)
