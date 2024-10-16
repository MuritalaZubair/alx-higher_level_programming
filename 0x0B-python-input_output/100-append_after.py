#!/usr/bin/python3
"""Module to append text after a specific line in a file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts new_string after each line containing search_string in filename."""
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
