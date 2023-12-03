#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for string in matrix:
        if len(string) == 0:
            print()
        for i in range(len(string)):
            if i is len(string) - 1:
            print("{:d}".format(string[i]), end="\n")
            else:
                print("{:d}".format(string[i]), end=" ")
