#!/usr/bin/python3
"""Defines function to write files."""


def write_file(filename="", text=""):
    """Write string to UTF8 text file.
    Args:
        filename (str): Name of file to write.
        text (str): Text to write to file.
        Returns:
            Number of written characters.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
