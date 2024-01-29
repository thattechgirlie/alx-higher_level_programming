#!/usr/bin/python3
"""Define class Rectangle."""


class Rectangle:
    """Representing a rectangle.

    Attributes:
        number_of_instances (int): Number of Rectangle instances.
        print_symbol (any): Symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize new Rectangle.

        Args:
            width (int): Width of nre rectangle.
            height: Height of new rectangkle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width of Rectangle."""
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise valueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of Rectangle."""
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perimeter of Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return greater are Rectangle.
        Args:
            rect_1 (Rectangle): First Rectangle.
            rect_2 (Rectangle): Second Rectangle.
            TypeError: If either rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
    
    @classmethod
    def square(cls, size=0):
        """Return new Rectangle with width and height equal to size.
        Args:
            size (int): Width and height of new Rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """Return print of Rectangle.
        Represents rectangle with # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for a in range(self.__height):
            [rect.append('#') for b in range(self.__width)]
            if a != self.__height - 1:
                rect.append("\n")
            return ("".join(rect))
    def __repr__(self):
        """Return string representation."""
        rect = "Rectangle(" + str(self.width)
        rect += ", " + str(self._height) + ")"
        return (rect)

    def __del__(self):
        """Print message for deletion of Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
