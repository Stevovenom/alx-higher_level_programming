#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints the full  name consisting of the first name and the last name.

    Args:
    first_name (str): The first name.
    last_name (str, optional): last name.

    Returns:
    None: This function does not return a valu.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
