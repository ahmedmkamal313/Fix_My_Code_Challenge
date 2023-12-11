#!/usr/bin/python3
""" square.py """


class Square():
    """ This class represents a square """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
        Initializes the square

        Args:
            width (int): The width of the square.
            height (int): The height of the square.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """
        Area of the square

        Returns:
            int: The area of the square.
        """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """
        Calculates the perimeter of the square.

        Returns:
            int: The perimeter of the square.
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """ Return a string """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
