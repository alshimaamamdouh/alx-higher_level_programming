#!/usr/bin/python3
'''square module'''


class Square:
    '''A class that represents a square'''
    def __init__(self, size):
        """Initialises the data"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def calculate_area(self):

        """
        Calculates the area of the square.

        Returns:
        float: The area of the square.
        """
        return self.side_length ** 2
