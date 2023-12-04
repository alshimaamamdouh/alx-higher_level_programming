#!/usr/bin/python3
"""
task 1
"""


class MyList(list):

    def print_sorted(self):
        """sorted a list"""

        print(sorted(list(self)))
