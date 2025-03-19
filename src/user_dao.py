from src.database import get_connection
from typing import Optional, Dict

def add_user(first_name: str, last_name: str, email: str, password: str, role_id: int) -> None:
    """
    Adds a new user to the database if the email doesn't already exist.

    :param first_name: The first name of the user.
    :param last_name: The last name of the user.
    :param email: The email address of the user.
    :param password: The password of the user.
    :param role_id: The role ID (admin or user).
    :return: None
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            # Check if the email already exists
            cur.execute("SELECT id FROM users WHERE email = %s", (email,))
            existing_user = cur.fetchone()
            if existing_user:
                print(f"User with email {email} already exists. Skipping insertion.")
                return  # Exit the function

            # Store password as plaintext 
            cur.execute("""
                INSERT INTO users (first_name, last_name, email, password, role_id)
                VALUES (%s, %s, %s, %s, %s)
            """, (first_name, last_name, email, password, role_id))
        conn.commit()  # Save changes


def get_user_by_email(email: str) -> Optional[Dict[str, str]]:
    """
    Retrieves user details by email.

    :param email: The email of the user.
    :return: A dictionary containing user details or None if not found.
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, first_name, last_name, email, password, role_id FROM users WHERE email = %s", (email,))
            user = cur.fetchone()
            if user:
                return {
                    "id": user[0],
                    "first_name": user[1],
                    "last_name": user[2],
                    "email": user[3],
                    "password": user[4],  
                    "role_id": user[5]
                }
    return None
