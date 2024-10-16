#!/usr/bin/python3
"""Module for writing an object to a text file using JSON."""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a file in JSON format.

    Args:
        my_obj: The object to be written to the file.
        filename (str): The name of the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
