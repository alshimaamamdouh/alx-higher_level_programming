#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    final = []
    for x in matrix:
        ret = []
        for y in x:
            ret.append(y ** 2)
        final.append(ret)
    return (final)
