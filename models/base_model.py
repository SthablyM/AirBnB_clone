#!/usr/bin/python3
"Defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Represent BaseModel"""
    def __init__(self, *args, **kwargs):
        timform = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for k, v in kwargs.items():
                if key == __class__:
                    continue
                elif key == "created_at" or "updated_at":
                    setattr(self, datetime.strptime(v, timform))
                else:
                    setattr(self, v, k)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

        models.storage.new(self)

    def save(self):
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        indict = self.__dict__.copy()
        indict["__class__"] = self.__class__.__name__
        indict["created_at"] = self.created_at.isoformat()
        indict["updated_at"] = self.updated_at.isoformat()
        return indict

    def __str__(self):
        classname = self.__dict__.copy()
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)


class My_First_Model:
    def __init__(self, instance_id):
        self.instance_id = instance_id
