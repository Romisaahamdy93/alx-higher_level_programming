#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for i in my_list:
            if idx < x:
                print("{}".format(my)list[i], end="")
                i += 1
        print()
    except TypeError:
        pass
    finally:
        return i
