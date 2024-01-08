#!/usr/bin/python3
"""Returns the list of available attributes."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
        obj (object): the object to list.
    """
    return dir(obj)
