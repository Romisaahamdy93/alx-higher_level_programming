#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for e in matrix:
        if len(e) == 0:
            print()
        for i in range(len(e)):
            print("{:d}".format(e[i]),
                  end="\n" if i is len(e) - 1 else " ")
