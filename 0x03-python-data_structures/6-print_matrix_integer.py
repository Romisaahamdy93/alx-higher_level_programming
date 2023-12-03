#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for element in matrix:
        if len(element) == 0:
            print()
        for i in range(len(element)):
             print("{:d}".format(element[i]),
                  end="\n" if i is len(element) - 1 else " ")

