#!/usr/bin/python3
"""Module for converting an object to its JSON string representation."""

import json


def to_json_string(my_obj):
    """Convert an object to its JSON string representation.

    Args:
        my_obj: The object to convert (can be a list, dictionary, string, etc.).

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
