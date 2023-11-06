#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        index = 0
        for val in row:
            if index == len(row) - 1:
                print("{:d}".format(val), end="")
            else:
                print("{:d}".format(val), end=" ")
            index += 1
        print()
