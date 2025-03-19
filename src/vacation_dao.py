from src.database import get_connection
from typing import List, Dict, Optional
from datetime import date


def request_vacation(user_id: int, country_id: int, start_date: str, end_date: str, price: float, image_file: str) -> None:
    """
    Inserts a new vacation into the vacations table.

    :param user_id: The ID of the user requesting the vacation.
    :param country_id: The country where the vacation takes place.
    :param start_date: The vacation start date.
    :param end_date: The vacation end date.
    :param price: The vacation cost.
    :param image_file: The filename of the vacation image.
    :return: None
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO vacations (country_id, description, start_date, end_date, price, image_file)
                VALUES (%s, 'Vacation', %s, %s, %s, %s)
            """, (country_id, start_date, end_date, price, image_file))
        conn.commit()  # Ensure changes are saved


def like_vacation(user_id: int, vacation_id: int) -> None:
    """
    Adds a like for a vacation by a user.

    :param user_id: The ID of the user liking the vacation.
    :param vacation_id: The ID of the vacation being liked.
    :return: None
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO likes (user_id, vacation_id) VALUES (%s, %s)
                ON CONFLICT DO NOTHING
            """, (user_id, vacation_id))
        conn.commit()


def unlike_vacation(user_id: int, vacation_id: int) -> None:
    """
    Removes a like from a vacation by a user.

    :param user_id: The ID of the user unliking the vacation.
    :param vacation_id: The ID of the vacation being unliked.
    :return: None
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM likes WHERE user_id=%s AND vacation_id=%s", (user_id, vacation_id))
        conn.commit()


def get_vacations() -> List[Dict[str, str]]:
    """
    Retrieves all vacation details, including country names instead of country IDs.

    :return: A list of dictionaries, each containing vacation details.
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT v.id, c.country_name, v.description, v.start_date, v.end_date, 
                       v.price, v.image_file
                FROM vacations v
                JOIN countries c ON v.country_id = c.id
                ORDER BY v.start_date ASC;
            """)
            vacations = cur.fetchall()

    # Convert results into a list of dictionaries with meaningful field names
    vacation_list = [
        {
            "id": v[0],
            "country": v[1],  # Returns country name instead of country_id
            "description": v[2],
            "start_date": v[3].strftime('%Y-%m-%d'),  # Format date as string
            "end_date": v[4].strftime('%Y-%m-%d'),
            "price": float(v[5]),  # Ensure price is returned as a float
            "image_file": v[6]
        }
        for v in vacations
    ]

    return vacation_list
