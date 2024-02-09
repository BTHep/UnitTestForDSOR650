import sys
import os
import unittest
import sqlite3
import tempfile  # Missing import added
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_storage import save_data_to_file, load_data_from_file, store_data_in_db

class TestDataStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup for database tests
        cls.test_db_path = tempfile.NamedTemporaryFile(delete=False).name
        cls.conn = sqlite3.connect(cls.test_db_path)
        cursor = cls.conn.cursor()
        cursor.execute('''CREATE TABLE test_table (id INTEGER PRIMARY KEY, value TEXT)''')
        cls.conn.commit()

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()
        os.unlink(cls.test_db_path)  # Clean up the test database file

    def test_save_and_load_data_to_file(self):
        """Test saving and loading data using pickle."""
        test_data = {'key': 'value', 'number': 42}
        temp_file = tempfile.NamedTemporaryFile(delete=False).name
        try:
            save_data_to_file(test_data, temp_file)
            loaded_data = load_data_from_file(temp_file)
            self.assertEqual(test_data, loaded_data)
        finally:
            os.unlink(temp_file)  # Clean up the temporary file

    def test_store_data_in_db(self):
        """Test storing data in the SQLite database."""
        data = [(1, 'One'), (2, 'Two')]
        table_name = 'test_table'
        store_data_in_db(data, self.test_db_path, table_name)

        # Verify the data was inserted into the database
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        fetched_data = cursor.fetchall()
        self.assertEqual(len(data), len(fetched_data))
        for original, fetched in zip(data, fetched_data):
            self.assertEqual(original, fetched)

if __name__ == '__main__':
    unittest.main()
