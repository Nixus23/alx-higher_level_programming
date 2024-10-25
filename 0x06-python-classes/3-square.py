#!/usr/bin/python3
""" A class Square that defines a square """


class Square():
    """ A class square with private attribute size
        A public instance method returning the area
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be an integer')
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
