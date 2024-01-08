#!/usr/bin/python3
"""Module for MyList class."""

class MyList(list):
    """A subclass."""
    def __init__(self):
        """Initialize object."""
        super().__init__()


    def print_sorted(self):
        """Prints the list, but sorted."""
        print(sorted(self))
