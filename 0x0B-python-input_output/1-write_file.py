#!/usr/bin/python3
"""Defines Write_file module."""


def write_file(filename="", text=""):
    """Writing the string to an UTF8 text"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
