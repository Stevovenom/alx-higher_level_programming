#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        a = 1
        for j in i:
            if a == len(i):
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
            a = a + 1
            print()
