#!/usr/bin/python3
"""Defines Unittests for city.py"""
import os
import models
import unittest
from datetime import datetime
from models.city import City


class TestCityInstantion(unittest.TestCase):
    """Unittest for testing instantiation of the city"""
    def test_no_args(self):
        self.assertEqual(City, type(City()))

    def test_id_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_name(self):
        c = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(c))
        self.assertNotIn("name", c.__dict__)
    
    def test_arg_unused(self):
        c = City(None)
        self.assertNotIn(None, c.__dict__.values())


class Test_City_save(unittest.TestCase):
    """Unittest testing for save of the class"""

    @classmethod
    def test_save_update(self):
        c = City()
        c.save()
        cid = "City." + c.id
        with open("file.json", "r") as file:
            self.assertIn(cid, file.read())

if __name__ == "__name__":
    unittest.main()

