#!/usr/bin/python3
"""defines a class called Square"""


class Square:
    """Initialize a Square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Define the size property of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the size property of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints a square based on size using #"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
