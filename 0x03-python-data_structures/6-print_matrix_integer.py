#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for x in i:
            print('{:d} '.format(x), end='')
        print()


def gt(matrix=[[]]):
    for i in matrix:
        print(' '.join('{:d}'.format(j)for j in i))


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()


gt(matrix)
print("--")
gt()
