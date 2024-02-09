import sqlite3
import os

def retrieve_data(db_path):
    try:
        # Ensure the path is correct
        print(f"Connecting to database at: {db_path}")
        print(f"Current working directory: {os.getcwd()}")

        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Define your SQL query
        query = "SELECT * FROM Location_Weather"

        # Execute the query and fetch all results
        cursor.execute(query)
        data = cursor.fetchall()

        # Close the database connection
        conn.close()

        return data
    except sqlite3.Error as e:
        print(f"Error: {e}")
        raise e
