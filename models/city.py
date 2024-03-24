#!/usr/bin/python3
"""Define the city"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent City
    Attributes:
        state_id (str):
            state id
        name (str):
            the name of the city"""

    state_id = ""
    name = ""
