#!/usr/bin/python3
"""Defines class rectangle."""
from models.base import Base


class Rectangle(Base):
    """Represent rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Imitialize new Rectangle.
        Args:
            width (int): Width of new Rectangle.
            height (int): Height of new Rectangle.
            x (int): Coordinate of new Rectangle.
            y (int): Coordinate of new Rectangle.
            id (int): Identity of new Rectangle.
        Raises:
            TypeError: If either width or height is not an int.
            ValueError: If either width or height <= 0.
            TypeError: If either x or y is not an int.
            ValueError: If either x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height of Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x coordinate of Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y coordinate of Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area of Rectangle."""
        return self.width * self.height

    def display(self):
        """Print Rectangle using `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update Rectangle.
        Args:
            *args (int): New attribute value.
                - 1st arg is id attribute
                - 2nd arg is width attribute
                - 3rd arg is height attribute
                - 4th arg is x attribute
                - 5th arg is y attribute
            **kwargs (dict): New key pairs of attributes.
        """
        if args and len(args) != 0:
            r = 0
            for arg in args:
                if r == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif r == 1:
                    self.width = arg
                elif r == 2:
                    self.height = arg
                elif r == 3:
                    self.x = arg
                elif r == 4:
                    self.y = arg
                r += 1
        elif kwargs and len(kwargs) != 0:
            for k, a in kwargs.items():
                if k == "id":
                    if a is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = a
                elif k == "width":
                    self.width = a
                elif k == "height":
                    self.height = a
                elif k == "x":
                    self.x = a
                elif k == "y":
                    self.y = a

    def to_dictionary(self):
        """Return dictionary representation of Rectangle."""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
        }

    def __str__(self):
        """Return print() and str() rep of Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
