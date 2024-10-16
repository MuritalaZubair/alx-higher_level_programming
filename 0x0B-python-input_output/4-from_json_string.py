#!/usr/bin/python3
"""Module for converting JSON strings to Python objects."""

import json


def from_json_string(my_str):
    """Convert a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        The Python object represented by the JSON string.
    """
    return json.loads(my_str)
