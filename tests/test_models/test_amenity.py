#!/usr/bin/python3
"""Defines Unittest of amenity"""
import os
import models
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenityInstantion(unittest.TestCase):
    """Unittests for testing instantion of the Amenity"""
    def test_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_id_str(self):
        self.assertEqual(str, type(Amenity().id))
    
    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))
    
    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name(self):
        my = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", my.__dict__)

    def test_args_unused(self):
        my = Amenity(None)
        self.assertNotIn(None, my.__dict__.values())

    def test_test_twounique_ids(self):
        myid1 = Amenity()
        myid2 = Amenity()
        self.assertNotEqual(myid1.id, myid2.id)


class TestAmenity_to_dict(unittest.TestCase):
    """Unittest for testing to_dict method"""
    def test_to_dict(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def testConstract_to_dict(self):
        my = Amenity()
        self.assertNotEqual(my.to_dict(), my.__dict__)


    def tet_updatefile(self):
        my = Amenity()
        my.save()
        myid = "Amenity." + my.id
        with open("file.json", "r") as file:
            self.assertIn(myid, file.read())

class TestAmenity_to_dict(unittest.TestCase):
    """Umiitest testing to_dictbmethod"""
    def test_to_dict(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def testConstrac_to_dict(self):
        my = Amenity()
        self.assertNotEqual(my.to_dict(), my.__dict__)

    


if __name__ == "__main__":
    unittest.main()

