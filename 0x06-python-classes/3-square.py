#!/usr/bin/python3
'''square module'''


class Square:
    '''empty class Square that defines a square'''
    def __init__(self, size=0):
        '''Initialises the data'''
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''Returns square area'''
        return self.__size**2
