import unittest
from database.db_manager import connect
class TestDB(unittest.TestCase):
    def test_connection(self):
        conn = connect()
        self.assertIsNotNone(conn)
        conn.close()
if __name__ == "__main__":
    unittest.main()
