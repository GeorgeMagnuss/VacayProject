import unittest
from datetime import datetime
from src.vacation_dao import request_vacation
from src.database import get_connection
from psycopg.errors import CheckViolation

class TestVacationDao(unittest.TestCase):
    def setUp(self):
        """Ensure test isolation by removing test vacations before each run."""
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM vacations WHERE description = 'Vacation'")

    def test_request_vacation(self):
        """Test inserting a new vacation with valid data"""
        result = request_vacation(1, 5, "2025-07-01", "2025-07-15", 1500.00, "beach_resort.jpg")
        self.assertIsNone(result)  # Expecting None on success

    def test_invalid_date_vacation(self):
        """Test that inserting a vacation with invalid dates fails"""
        with self.assertRaises(CheckViolation):
            request_vacation(1, 5, "2023-07-01", "2023-07-15", 1500.00, "beach_resort.jpg")

    def test_invalid_price_vacation(self):
        """Test that inserting a vacation with an invalid price fails"""
        with self.assertRaises(CheckViolation):
            request_vacation(1, 5, "2025-07-01", "2025-07-15", 10001, "beach_resort.jpg")

if __name__ == '__main__':
    unittest.main()
