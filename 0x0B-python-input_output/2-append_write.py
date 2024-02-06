#!/usr/bin/python3
"""Define function to append files."""


def append_write(filename="", text=""):
    """Append string to end of UTF8 text file.
    Args:
        filename (str): Name of file to append.
        text (str): String to append file.
    Returns:
        Number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
