#!/usr/bin/python3
# 0-square_matrix_simple.py

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[x ** 2 for x in row] for row in matrix]
    return new_matrix
