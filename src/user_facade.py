from src.user_dao import add_user, get_user_by_email
from src.vacation_dao import like_vacation as dao_like_vacation, unlike_vacation as dao_unlike_vacation
from typing import Optional


def register_user(first_name: str, last_name: str, email: str, password: str, role_id: int) -> None:
    """
    Registers a new user with validation checks.

    :param first_name: The first name of the user.
    :param last_name: The last name of the user.
    :param email: The email address of the user.
    :param password: The password of the user.
    :param role_id: The role ID of the user (defaults to 2 for regular users).
    :return: None
    """
    if len(password) < 4:
        raise ValueError("Password must be at least 4 characters.")
    if not email:
        raise ValueError("Email is required.")
    if not first_name or not last_name:
        raise ValueError("First name and last name are required.")
    
    return add_user(first_name, last_name, email, password, role_id=2)  # Always create regular users


def login_user(email: str, password: str) -> Optional[int]:
    """
    Authenticates a user by checking their email and password.
    Returns the user ID if successful, else returns None.

    :param email: The email address of the user.
    :param password: The password entered by the user.
    :return: The user ID if login is successful, otherwise None.
    """
    user = get_user_by_email(email)
    if user and user["password"] == password:  # Simple plaintext comparison
        print(f"User {email} logged in successfully.")
        return user["id"]  # Return user ID if login is successful
    else:
        print("Invalid email or password.")
        return None


def like_vacation(user_id: int, vacation_id: int) -> None:
    """
    Calls the DAO function to like a vacation.

    :param user_id: The ID of the user liking the vacation.
    :param vacation_id: The ID of the vacation being liked.
    :return: None
    """
    return dao_like_vacation(user_id, vacation_id)  # Correct function call


def unlike_vacation(user_id: int, vacation_id: int) -> None:
    """
    Calls the DAO function to unlike a vacation.

    :param user_id: The ID of the user unliking the vacation.
    :param vacation_id: The ID of the vacation being unliked.
    :return: None
    """
    return dao_unlike_vacation(user_id, vacation_id)  # Correct function call
