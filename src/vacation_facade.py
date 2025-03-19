from src.database import get_connection

def like_vacation(user_id: int, vacation_id: int) -> None:
    """
    Allows a user to like a vacation, preventing duplicate likes.

    :param user_id: The ID of the user liking the vacation.
    :param vacation_id: The ID of the vacation being liked.
    :return: None
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO likes (user_id, vacation_id) 
                VALUES (%s, %s) 
                ON CONFLICT DO NOTHING
            """, (user_id, vacation_id))
            conn.commit()


def unlike_vacation(user_id: int, vacation_id: int) -> None:
    """
    Allows a user to remove their like from a vacation.

    :param user_id: The ID of the user unliking the vacation.
    :param vacation_id: The ID of the vacation being unliked.
    :return: None
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                DELETE FROM likes WHERE user_id=%s AND vacation_id=%s
            """, (user_id, vacation_id))
            conn.commit()
