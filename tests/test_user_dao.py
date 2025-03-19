import unittest
from src.user_dao import add_user
from src.database import get_connection

class TestUserDao(unittest.TestCase):
    def setUp(self) -> None:
        """Ensure test isolation by removing the test user before each run."""
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM users WHERE email = 'unique@example.com'")
    
    def test_create_user(self) -> None:
        """Test inserting a new user with a unique email."""
        result = add_user('Test', 'User', 'unique@example.com', 'pass123', 2)  # Unique email
        self.assertIsNone(result)  # Ensure that the function does not return anything.

if __name__ == '__main__':
    unittest.main()
