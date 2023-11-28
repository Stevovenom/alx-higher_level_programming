#!/usr/bin/python3
for numbers in range(10):
    for digits in range(numbers + 1, 10):
        if numbers == 8 and digits == 9:
            print("{}{}".format(numbers, digits))
        else:
            print("{}{}".format(numbers, digits), end=", ")
