#!/usr/bin/python3
"""defines a class called sqaure"""


class Square:
    """a class called square"""

    def __init__(self, size=0):
        """initialize the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)
