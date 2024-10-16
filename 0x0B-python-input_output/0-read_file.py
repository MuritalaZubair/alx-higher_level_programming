#!/usr/bin/python3
"""The module define a text file-reading function"""


def read_file(filename=""):
    """Prints the contents of a UTF8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
