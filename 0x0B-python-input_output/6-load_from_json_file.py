#!/usr/bin/python3
"""Module for creating an object from a JSON file."""

import json


def load_from_json_file(filename):
    """Read a JSON file and create an object.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        The Python object represented by the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
