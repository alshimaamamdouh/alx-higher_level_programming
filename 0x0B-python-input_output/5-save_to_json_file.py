#!/usr/bin/python3
"""
task 5
"""


def save_to_json_file(my_obj, filename):
    """save"""
    import json
    with open(filename, 'w', encoding='utf-8') as file_j:
        json.dump(my_obj, file_j)
