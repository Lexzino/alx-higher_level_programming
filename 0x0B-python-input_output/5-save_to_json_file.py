#!/usr/bin/python3

"""Defining the JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file.
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f, ensure_ascii=False)
