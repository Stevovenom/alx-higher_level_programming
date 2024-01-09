#!/usr/bin/python3
class MyInt(int):
    """
    A class representing an integer with inverted equality and inequality operators.
    """

    def __eq__(self, other):
        """
        Overrides the equality operator (==) to return the opposite of the default behavior.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator (!=) to return the opposite of the default behavior.
        """
        return super().__eq__(other)

