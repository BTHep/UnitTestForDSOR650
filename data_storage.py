import pickle
import sqlite3

def save_data_to_file(data, file_path):
    """
    Serialize and save data to a file using pickle.

    Parameters:
    - data: The Python object to serialize and save.
    - file_path: The path to the file where the data should be saved.
    """
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

def load_data_from_file(file_path):
    """
    Load and deserialize data from a file using pickle.

    Parameters:
    - file_path: The path to the file from which to load the data.

    Returns:
    - The deserialized Python object.
    """
    with open(file_path, 'rb') as file:
        return pickle.load(file)

def store_data_in_db(data, db_path, table_name):
    """
    Store data in an SQLite database.

    Parameters:
    - data: A list of tuples representing the data to be stored.
    - db_path: The path to the SQLite database file.
    - table_name: The name of the table where data will be inserted.

    Note: This function assumes that the structure of the tuples in `data`
    matches the column structure of `table_name`.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Construct a query string with placeholders for data insertion
        placeholders = ', '.join(['?'] * len(data[0]))
        query = f'INSERT INTO {table_name} VALUES ({placeholders})'
        
        # Execute the query and commit changes
        cursor.executemany(query, data)
        conn.commit()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        raise e
    finally:
        if conn:
            conn.close()
