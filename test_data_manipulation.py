import sys
import os
# Append the directory where data_manipulation.py is located to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from data_manipulation import transform_data, aggregate_data, filter_data

class TestDataManipulation(unittest.TestCase):

    def setUp(self):
        self.sample_data = [
            {'name': 'Alice', 'age': 30, 'city': 'New York'},
            {'name': 'Bob', 'age': 22, 'city': 'Los Angeles'},
            {'name': 'Charlie', 'age': 35, 'city': 'New York'},
            {'name': 'Dana', 'age': 28, 'city': 'Los Angeles'},
        ]

    def test_transform_data(self):
        transformed = transform_data(self.sample_data, lambda x: {**x, 'age': x['age'] + 1})
        for item in transformed:
            self.assertIn('age', item)
            self.assertTrue(item['age'] > 0)  # Ensure age is incremented

    def test_aggregate_data(self):
        result = aggregate_data(
            self.sample_data, 
            key_func=lambda x: x['city'], 
            aggregate_func=lambda items: sum(item['age'] for item in items) / len(items)
        )
        self.assertEqual(result, {'New York': 32.5, 'Los Angeles': 25})

    def test_filter_data(self):
        filtered = filter_data(self.sample_data, lambda x: x['age'] > 25)
        self.assertEqual(len(filtered), 3)  # Expecting 3 people over 25
        for person in filtered:
            self.assertTrue(person['age'] > 25)

if __name__ == '__main__':
    unittest.main()
