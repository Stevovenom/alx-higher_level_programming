#!/usr/bin/python3
for numbers in range(10):
    for digits in range(numbers + 1, 10):
        print(f'{numbers}{digits}', end=", " if (numbers, digits) != (8, 9)
              else "\n")
