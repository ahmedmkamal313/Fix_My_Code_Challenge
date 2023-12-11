#!/usr/bin/python3
"""
User class
"""


class User():
    """A class to represent a user.

    Attributes:
        email (str): The email address of the user.
    """

    def __init__(self, email):
        """Initialize the user with an email.

        Args:
            email (str): The email address of the user.

        Raises:
            TypeError: If email is not a string.
        """
        self.__email = email

    @property
    def email(self):
        """Get the email address of the user.

        Returns:
            str: The email address of the user.
        """
        return self.__email

    @email.setter
    def email(self, value):
        """Set the email address of the user.

        Args:
            value (str): The new email address of the user.

        Raises:
            TypeError: If value is not a string.
        """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value
