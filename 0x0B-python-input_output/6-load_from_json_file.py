#!/usr/bin/python3
"""load from json."""
import json


def load_from_json_file(filename):
    """Developing Python object from  JSON file."""
    with open(filename) as f:
        return json.load(f)
