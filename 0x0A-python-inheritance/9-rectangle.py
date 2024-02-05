#!/usr/bin/python3
"""Define class Rectangle inherited from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent rectangle with BaseGeometry."""
    def __init__(self, width, height):
        """Initialize new Rectangle.
        Args:
            width (int): Width of new Rectangle.
            height (int): Height of new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validatot("height", height)
        self.__height = height

    def area(self):
        """Return area of Rectangle."""
        return self.__width * self.__height
    def __str__(self):
        """Return print() and str() representation of Rectangle."""
        string = "[" + str(self.__class__.name__) + "] "
        string += str(self.width.__width) + "/" + str(self.__height)
        return string
