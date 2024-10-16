#!/usr/bin/python3
"""Module that provides a function to convert a class instance to a JSON-compatible dictionary."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure 
    for JSON serialization of an object.
    """
    return obj.__dict__
