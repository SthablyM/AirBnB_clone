#!/usr/bin/python3
"""Define the Filestorage"""
import json 
import os 
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """Represent  Storage  engine
    Attributes:
    __object (dict): A dictionary of instantiated object.
    __file_path (str): name of the file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the __ a dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in obj with a key"""
        obclname = obj.__class__.__name__
        key = "{}, {}".format(obclname, obj, id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        allobj = FileStorage.__objects
        objectdic = {}
        for o in allobj.keys():
            objectdic[o] = allobj[o].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(objectdic, f)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    objectdic = json.load(file)
                    for key,  v in objectdic.items():
                        clname, object_id = key.split('.')

                        clas = eval(clname)
                        i =  clas(**v)
                        FileStorage.__object[key] = i

                except Exception:
                    pass
