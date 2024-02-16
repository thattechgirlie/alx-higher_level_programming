#!/usr/bin/python3
"""Define class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize new Square.
        Args:
            size (int): Size of new Square.
            x (int): Coordinate of new Square.
            y (int): Coordinate of new Square.
            id (int): Identity of new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Set size of Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update Square.
            Args:
                 *args (int): New attribute value.
                - 1st arg is id attribute
                - 2nd arg is size attribute
                - 3rd arg is x attribute
                - 4th arg is y attribute
            **kwargs (dict): New key pairs of attributes.
        """
        if args and len(args) != 0:
            r = 0
            for arg in args:
                if r == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif r == 1:
                    self.size = arg
                elif r == 2:
                    self.x = arg
                elif r == 3:
                    self.y = arg
                r += 1
        elif kwargs and len(kwargs) != 0:
            for k, a in kwargs.items():
                if k == "id":
                    if a is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = a
                elif k == "size":
                    self.size = a
                elif k == "x":
                    self.x = a
                elif k == "y":
                    self.y = a

    def to_dictionary(self):
        """Return dictionary representation of Square."""
        return {
                "id": self.id,
                "width": self.width,
                "x": self.x,
                "y": self.y
        }

    def __str__(self):
        """Return print() and str() rep of Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
