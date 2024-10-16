#!/usr/bin/python3
"""Module that provides a function to append text to a file."""


def append_write(filename="", text=""):
    """Appends a given string to the end of a text file (UTF8) and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    # Use 'with' statement to ensure proper file handling
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
