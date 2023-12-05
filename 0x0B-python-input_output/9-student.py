#!/usr/bin/python3
"""
task 9
"""


class Student:
    """ student """

    def __init__(self, first_name, last_name, age):
        """ init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ set """
        return self.__dict__
