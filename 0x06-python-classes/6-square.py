"""Define class Square."""


class Square:
    """Represent square."""
    def __init__(self, size):
        """Initiliaze a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get current size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current area of square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square with # character."""
        for a in range(0, self.__size):
            [print("#", end="") for b in range(self.__size)]
            print("")
            if self.__size == 0:
                print("")
                return
            [print("") for a in range (0, self.__position[1])]
                for a in range(0, self.__size:
                    [print(" ", end="") for b in range(0, self.__position[0])]
                    print("#", end="") for c in range(0, self.__size)]
                    print("")
