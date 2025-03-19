from src.database import get_connection
from typing import List, Optional, Any

class BaseDAO:
    table_name: str

    def get_all(self) -> List[Any]:
        """
        Retrieve all records from the table.

        :return: A list of all records from the table.
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(f'SELECT * FROM {self.table_name}')
                return cur.fetchall()

    def get_by_id(self, record_id: int) -> Optional[Any]:
        """
        Retrieve a single record by ID.

        :param record_id: The ID of the record to retrieve.
        :return: The record corresponding to the ID, or None if not found.
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(f'SELECT * FROM {self.table_name} WHERE id=%s', (record_id,))
                return cur.fetchone()

    def delete_by_id(self, record_id: int) -> None:
        """
        Delete a record by ID.

        :param record_id: The ID of the record to delete.
        :return: None
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(f'DELETE FROM {self.table_name} WHERE id=%s', (record_id,))
                conn.commit()
