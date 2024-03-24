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
        self.assertEqual(datetime, type(Place).created_at)

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

    def test_numberofrooms(self):
        plc = Place()
        self.assertEqual(int, type(Place.numberofrooms))
        self.assertIn("numberofrooms", dir(plc))
        self.assertNotIn("numberofrooms", plc.__dict__)

    def test_numberOfBathrooms(self):
        plc = Place()
        self.assertEqual(int, type(place.numberOfBathrooms))
        self.asserIn("numberOfBathrooms", dir(plc))
        self.assertNotIn("numberOfBathrooms", plc.__dict)

    def test_guest(self):
        plc = Place()
        self.assertEqual(int, type(Place.guest))
        self.assertIn("guest", dir(plc))
        self.assertNotIn("guest", plc.__dict__)



class Test_Place_save(unittest.TestCase):
    """Unittest testing for save of the class"""

    @classmethod

    def test_save_update(self):
        plc = Place()
        plc.save()
        plcid = "Place." + c.id
        with open("file.json", "r") as file:
            self.assertIn(plcid, file.read())


class TestPlace_to_dict(unittest.TestCase):
    """Unittest for testing to_dict method of the city"""

    def test_to_dict(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_datetime(self):
        plc = Place()
        plc.name = "Holberton"
        plc.number = 98
        self.assertEqual("Holberton", plc.name)
        self.assertIn("my_number", plc.to_dict)


if __name__ == "__name__":
    unittest.main()

