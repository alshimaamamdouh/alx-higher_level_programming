#!/usr/bin/python3
"""
task 7
"""


import sys
import json

def save_to_json_file(my_obj, filename):
    """ save """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file, ensure_ascii=False, indent=4)


def load_from_json_file(filename):
    """ load """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


existing_data = load_from_json_file("add_item.json")
arguments = sys.argv[1:]
existing_data.extend(arguments)
save_to_json_file(existing_data, "add_item.json")
