import sys
import unittest
import sqlite3
# Add the directory containing data_retrieval.py to the Python path
sys.path.append('/Users/benhepner/Documents/VSCODE')
from data_retrieval import retrieve_data

class TestDataRetrieval(unittest.TestCase):
    def test_data_retrieval_success(self):
        """Test successful data retrieval from the database."""
        db_path = '/Users/benhepner/Downloads/Flight.db'  # Correct path to your database
        data = retrieve_data(db_path)
        # Assuming your database is not empty, check if data is returned
        self.assertTrue(len(data) > 0, "Data should be retrieved successfully.")

    def test_data_retrieval_failure(self):
        """Test data retrieval failure with an invalid database path."""
        db_path = 'non/existent/path/Flight.db'
        with self.assertRaises(sqlite3.OperationalError):
            retrieve_data(db_path)

if __name__ == '__main__':
    unittest.main()
