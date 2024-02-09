import logging
import sqlite3

# Setup basic configuration for logging
logging.basicConfig(level=logging.ERROR, filename='app_errors.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

class DataValidationError(Exception):
    """Exception raised for errors in the input data."""
    def __init__(self, message="Data is invalid"):
        self.message = message
        super().__init__(self.message)

class DatabaseError(Exception):
    """Exception raised for errors in database operations."""
    def __init__(self, message="Database operation failed"):
        self.message = message
        super().__init__(self.message)

def log_error(error):
    """Log an error message to the application's log file."""
    logging.error(f"Error: {error}")

def handle_error(func):
    """Decorator function for handling exceptions in a unified manner."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (sqlite3.DatabaseError, sqlite3.IntegrityError) as db_err:
            log_error(f"Database error occurred: {db_err}")
            raise DatabaseError("A database error occurred. Please try again.") from db_err
        except DataValidationError as data_err:
            log_error(f"Data validation error: {data_err}")
            raise
        except Exception as err:
            log_error(f"Unexpected error: {err}")
            raise Exception("An unexpected error occurred. Please contact support.") from err
    return wrapper
