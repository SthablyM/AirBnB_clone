#!/usr/bin/python3
"""Define Unittest for console.py"""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand


class Test_HBNBCommand_Prompt(unittest.TestCase):
    """Testing prompt of the HBNB command"""
    def tst_prmpt(self):
        self.assertEqual("(hbnb) ", HBNBCommand, prompt)

if __name__ == "__main__":
    unittest.main()
