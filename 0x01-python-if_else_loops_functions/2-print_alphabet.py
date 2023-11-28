#!/usr/bin/python3
first_letter = ord('a')
for offset in range(26):
    print(chr(first_letter + offset), end="")
