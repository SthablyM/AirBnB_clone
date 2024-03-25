#!/usr/bin/python3
"""Defines Unittests for place"""
import os
import models
import unittest
from datetime import datetime
from models.place import Place


class TestPlaceInstantion(unittest.TestCase):
    """Unittest for testing instantiation of the city"""
    def test_no_args(self):
        self.assertEqual(Place, type(Place()))

    def test_id_str(self):
        self.assertEqual(str, type(Place() .id))

    def test_created_at_datetime(self):
        place_instance = Place()
        created_at_value = place_instance.created_at
        self.assertIsInstance(created_at_value, datetime)

    def test_updated_at(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_name(self):
        plc = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(plc))
        self.assertNotIn("name", plc.__dict__)
    
    def test_arg_unused(self):
        plc = Place(None)
        self.assertNotIn(None, plc.__dict__.values())



if __name__ == "__name__":
    unittest.main()

