#!/usr/bin/python3
"""Define the Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent the review
    Attributes:
        place_id(str): The place_id
        user_id(str): The user_id
        text(str): The text of the review"""
    place_id = ""
    user_id = ""
    text = ""
