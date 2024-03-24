#!/usr/bin/python3
"""Define unittest for base_model.py"""
import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    """Unittest for testing BaseModel class"""
    def test__init__(self):
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        my_model = BaseModel()

        first_update_at = my_model.updated_at
        second_update_at = my_model.save()
        self.assertNotEqual(first_update_at, second_update_at)

    def test_to_dict(self):
        my_model = BaseModel()

        my_model_json = my_model.to_dict()
        self.assertIsInstance(my_model_json, dict)
    
    def test__str__(self):
        my_model = BaseModel()
        
        self.assertIn(my_model.id, str(my_model))


if __name__ == "__main__":
    unittest.main()
