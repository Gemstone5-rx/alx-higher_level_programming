#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square by: (based on 4-square.py).
    Attributes:
        size: square size (1 side).
    """
    def __init__(self, size=0):
        """Creates new instances of square.
        Args:
            size: square size (1 side).
        """
        self.__size = size

    def area(self):
        """Calculates the area of square.
        Returns: the current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Returns square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size.
        Args:
            value (int): square size (1 side).
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #
        """
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
