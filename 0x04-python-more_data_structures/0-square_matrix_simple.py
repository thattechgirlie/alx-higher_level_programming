#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    return list(list(map(lamda a:a*a, num_list)) for num_list in matrix)
