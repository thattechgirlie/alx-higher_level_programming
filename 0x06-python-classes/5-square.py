#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.size = size
    @property
    def size(self):
        return (self._size)
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        def area(self):
            return (self._size *self._size)
        def my_print(self):
            for a in range(0, self._size):
                [print("#", end="") for b in range(self._size)]
                print("")
            if self._size == 0:
                print("")
