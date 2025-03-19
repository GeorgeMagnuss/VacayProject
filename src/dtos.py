from dataclasses import dataclass
from enum import Enum
from datetime import date
from typing import Optional


class Role(Enum):
    ADMIN = 'admin'
    USER = 'user'


@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    email: str
    password: str
    role: Role

    def __init__(self, id: int, first_name: str, last_name: str, email: str, password: str, role: Role):
        """
        Initializes a new User object.

        :param id: The unique identifier for the user.
        :param first_name: The first name of the user.
        :param last_name: The last name of the user.
        :param email: The email address of the user.
        :param password: The password of the user.
        :param role: The role of the user (ADMIN or USER).
        """
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role = role


@dataclass
class Country:
    id: int
    country_name: str

    def __init__(self, id: int, country_name: str):
        """
        Initializes a new Country object.

        :param id: The unique identifier for the country.
        :param country_name: The name of the country.
        """
        self.id = id
        self.country_name = country_name


@dataclass
class Vacation:
    id: int
    country_id: int
    description: str
    start_date: date
    end_date: date
    price: float
    image_file: str

    def __init__(self, id: int, country_id: int, description: str, start_date: date, end_date: date, price: float, image_file: str):
        """
        Initializes a new Vacation object.

        :param id: The unique identifier for the vacation.
        :param country_id: The ID of the country associated with the vacation.
        :param description: A description of the vacation.
        :param start_date: The start date of the vacation.
        :param end_date: The end date of the vacation.
        :param price: The price of the vacation.
        :param image_file: The file name of the vacation image.
        """
        self.id = id
        self.country_id = country_id
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.image_file = image_file


@dataclass
class Like:
    user_id: int
    vacation_id: int

    def __init__(self, user_id: int, vacation_id: int):
        """
        Initializes a new Like object.

        :param user_id: The ID of the user who liked the vacation.
        :param vacation_id: The ID of the vacation that was liked.
        """
        self.user_id = user_id
        self.vacation_id = vacation_id
