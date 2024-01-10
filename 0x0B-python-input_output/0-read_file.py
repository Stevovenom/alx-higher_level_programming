#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
    - filename (str): The path to the text file.

    Raises:
    - FileNotFoundError: If the file specified by filename does not exist.
    - PermissionError: If the user does not have permission to read the file.

    Returns:
    - None
    """
    try:
        with open(filename, "r", encoding="UTF-8") as f:
            print(f.read(), end="")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'.")

