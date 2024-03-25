#!/usr/bin/python3
"""Defines Unittests for city.py"""
import os
import models
import unittest
from datetime import datetime
from models.review import Review


class TestReviewInstantion(unittest.TestCase):
    """Unittest for testing instantiation of the city"""
    def test_no_args(self):
        self.assertEqual(Review, type(Review()))

    def test_id_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_arg_unused(self):
        rev = Review(None)
        self.assertNotIn(None, rev.__dict__.values())

    def test_twoDifferentReview(self):
        rev1 = Review()
        rev2 = Review()
        self.assertNotEqual(rev1, rev2.id)

    

if __name__ == "__name__":
    unittest.main()

