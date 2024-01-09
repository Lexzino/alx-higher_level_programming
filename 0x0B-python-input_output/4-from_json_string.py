#!/usr/bin/python3
# 6-from_json_string.py
"""from_json_string module."""
import json


def from_json_string(my_str):
    """Returnin Python object representation for JSON string."""
    return json.loads(my_str)
