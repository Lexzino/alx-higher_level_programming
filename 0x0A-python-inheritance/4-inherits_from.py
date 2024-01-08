#!/usr/bin/python3
"""Defines an inherited class-checking method."""


def inherits_from(obj, a_class):
    """Checking  if the object is  inherited instance """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
