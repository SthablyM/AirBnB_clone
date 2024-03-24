#!/usr/bin/python3
"""Define User class"""
from models.base_model import BaseModel


 class User(BaseModel):
     """Class user that will handle user's information"""

     email = ""
     password = ""
     first_name = ""
     last_name = ""
