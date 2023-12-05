#!/usr/bin/python3
"""
task 2
"""


def append_write(filename="", text=""):
    """append"""
    with open(filename, "a", encoding="utf-8") as file_a:
        num = file_a.write(text)
        return num
