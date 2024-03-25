#!/usr/bin/python3
"""Define the place"""

from models.base_model import BaseModel

class Place(BaseModel):
    """Represent a place
    Attribut:
        city_id (str): THe city_id
        user_id (str): The user_id
        name (str): Name of the place
        description (str): The description of the place
        number_rooms (int): The number of the rooms
        number_bathrooms (int): ThE number of the bathrooms
        max_guest (int): The max_guest
        price_by_night (int): The price of the place at night
        latitude (float): The latitude of the place
        longitude (float): The longitude of the place
        amenity_ids (list): A list of Amenity ids"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
