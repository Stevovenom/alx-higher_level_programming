#!/usr/bin/python3

def read_file(filename=""):
    """Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str): The path to the text file.

    Returns:
        None
    """
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            print(file.read(), end="")
    except:
        pass
