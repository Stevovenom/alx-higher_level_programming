#!/usr/bin/python3
first_letter = ord('a')
for offset in range(26):
    letter = chr(first_letter + offset)
    if letter != 'q' and letter != 'e':
        print(letter, end="")
