#!/usr/bin/python3
"""Define inherited list class MyList."""


class MyList(list):
    """Sorts out printing for built in list class."""
    def print_sorted(self):
        """Print list in ascending order."""
        print(sorted(self))
