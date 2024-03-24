#!/usr/bin/python3
"""Defines Unittests for city.py"""
import os
import models
import unittest
from datetime import datetime
from models.state import State


class TestStateInstantion(unittest.TestCase):
    """Unittest for testing instantiation of the city"""
    def test_no_args(self):
        self.assertEqual(State, type(State()))

    def test_id_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name(self):
        s = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(s))
        self.assertNotIn("name", s.__dict__)
    
    def test_arg_unused(self):
        s = Statey(None)
        self.assertNotIn(None, s.__dict__.values())


class Test_State_save(unittest.TestCase):
    """Unittest testing for save of the class"""

    @classmethod

    def test_save_update(self):
        s = State()
        s.save()
        sid = "State." + s.id
        with open("file.json", "r") as file:
            self.assertIn(sid, file.read())


class TestState_to_dict(unittest.TestCase):
    """Unittest for testing to_dict method of the city"""

    def test_to_dict(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_datetime(self):
        s = State()
        s.name = "Holberton"
        s.number = 98
        self.assertEqual("Holberton", s.name)
        self.assertIn("my_number", s.to_dict)


if __name__ == "__name__":
    unittest.main()

