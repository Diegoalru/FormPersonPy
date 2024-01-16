"""
This module contains utility functions for the application.
"""


import re

def validate_email(email) -> bool:
    """
    Validates an email address.
    :param email: The email address to validate.
    :return: True if the email address is valid, False otherwise.
    """
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validate_phone(phone) -> bool:
    """
    Validates a phone number.
    :param phone: The phone number to validate.
    :return: True if the phone number is valid, False otherwise.
    """
    return re.match(r"^\d{8,10}$", phone)

def validate_age(age) -> bool:
    """
    Validates an age of a person.
    :param age: The age to validate.
    :return: True if the age is valid, False otherwise.
    """
    return re.match(r"^\d{1,3}$", age) and 0 < int(age) < 99
