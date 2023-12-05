#!/usr/bin/python3
"""
task 0
"""


def read_file(filename=""):
    """read file with UTF-8"""

    with open(filename, "r", encoding="UTF-8") as file_re:
        data = file_re.read()
        print(data, end="")
