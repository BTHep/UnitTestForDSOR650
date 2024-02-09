import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch
# Import from error_handling after adjusting sys.path
from error_handling import DataValidationError, DatabaseError, log_error, handle_error
import sqlite3

class TestErrorHandling(unittest.TestCase):

    @patch('error_handling.logging.error')
    def test_log_error(self, mock_logging_error):
        """Test that errors are logged correctly."""
        test_error_message = "Test error"
        log_error(test_error_message)
        mock_logging_error.assert_called_with(f"Error: {test_error_message}")

    def test_custom_exceptions(self):
        """Test custom exception messages."""
        with self.assertRaises(DataValidationError) as context:
            raise DataValidationError("Invalid data")
        self.assertEqual("Invalid data", str(context.exception))

        with self.assertRaises(DatabaseError) as context:
            raise DatabaseError("Database failure")
        self.assertEqual("Database failure", str(context.exception))

    @patch('error_handling.log_error')
    def test_handle_error_decorator_db_error(self, mock_log_error):
        """Test the handle_error decorator with a simulated database error."""

        @handle_error
        def mock_db_operation():
            raise sqlite3.IntegrityError("Integrity error")

        with self.assertRaises(DatabaseError):
            mock_db_operation()
        mock_log_error.assert_called()

    @patch('error_handling.log_error')
    def test_handle_error_decorator_data_validation_error(self, mock_log_error):
        """Test the handle_error decorator with a simulated data validation error."""

        @handle_error
        def mock_data_operation():
            raise DataValidationError("Invalid data provided")

        with self.assertRaises(DataValidationError):
            mock_data_operation()
        mock_log_error.assert_called()

if __name__ == '__main__':
    unittest.main()
