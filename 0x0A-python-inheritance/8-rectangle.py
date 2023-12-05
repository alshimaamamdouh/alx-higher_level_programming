#!/usr/bin/python3
"""
task 8
"""


class BaseGeometry():
    """BaseGeometry class"""

    def area(self):
        """Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ value """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """ Rectangle inherits from BaseGeomtry """

    def __init__(self, width, height):
        """ init """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
