#!/usr/bin/python3
"""Defines class Rectangle."""


class Rectangle:
    """Represent rectangle."""

    def __init__(self, height=0, width=0):
        """Initialize new Rectangle.

        Args:
            height (int): Height of new rectangle.
            width (int): Width of new rectangle.
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """Get height of Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be >= 0")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    @property
    def width(self):
        """Get width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Return area of Rectangle."""
        return (self.__height * self.__width)

    def perimeter(self):
        """Return perimeter of Rectangle."""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))
