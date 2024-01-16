"""
A module that represents a person.
"""

class Person:
    """
    A class that represents a person.
    """

    def __init__(self, name, email, phone, age):
        """
        Creates a Person object.
        :param name: Name of the person.
        :param email: Email of the person.
        :param phone: Phone number of the person.
        :param age: Age of the person.
        """
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age

    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        :return: A string representation of the object.
        """
        return f"Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\nAge: {self.age}\n"
