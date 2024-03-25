#!/usr/bin/python3
"""Define unittest for models/user.py"""
import os
import models
import models
import unittest
from datetime import datetime
from models.user import User
from time import sleep

class Test_User_Instatiation(unittest.TestCase):
    """Unittest for the testing instatiation of the User"""
    def test_no_args(self):
        self.assertEqual(User, type(User()))

    def test_id_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_email_str(self):
        self.assertEqual(str, type(User.password))

    def test_name(self):
        self.assertEqual(str, type(User.email))


if __name__ == "__main__":
    unittest.main()
