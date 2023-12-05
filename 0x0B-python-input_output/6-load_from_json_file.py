#!/usr/bin/python3
"""
task 6
"""


def load_from_json_file(filename):
    """load"""
    import json
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
