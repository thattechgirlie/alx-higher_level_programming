#!/usr/bin/python3
"""Define base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate parameter as integer.
        Args:
            name (str): Name of parameter.
            value (int): Parameter to validate.
            Raises:
                TypeError: If value is not an integer.
                ValueError: If value <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
