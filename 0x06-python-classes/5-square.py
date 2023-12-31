#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialization a new Square.

        Args:
            size: size of Square.
        """
        self.__size = size

    @property
    def size(self):
        """Property for current size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of square.

        Returns:
            The current square area.
        """
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size is 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
