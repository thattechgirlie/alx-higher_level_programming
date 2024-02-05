#!/usr/bin/python3
"""Defines Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representing square."""
    def __init__(self, size):
        """Initialize new square.
        Args:
            size (int): Size of new square.
        """
        self.integer_validator("size", size)
        super().__iinit__(size, size)
        self.__size = size
