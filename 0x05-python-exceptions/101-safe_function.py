#!/usr/bin/python3

import sys
def safe_function(fct, *args):
    try:
        r = fct(*args)
    except ZeroDivisionError:
        r = None
        sys.stderr.write("Exception: division by zero\n")
    except IndexError:
        r = None
        sys.stderr.write("Exception: list index out of range\n")
    return (r)
        
