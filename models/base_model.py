#!/usr/bin/python3
""" Base module """

import uuid
from datetime import datetime


class BaseModel:
    """ class which other classes will inherit from """

    def __init__(self, *args, **kwargs):
        """ initializes instances """

                if kwargs:
            self.__dict__.update(**kwargs)
            self.created_at = datetime.fromisoformat(kwargs["created_at"])
            self.updated_at = datetime.fromisoformat(kwargs["updated_at"])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = dict_copy["created_at"].isoformat()
        dict_copy["updated_at"] = dict_copy["updated_at"].isoformat()
        dict_copy["__class__"] = type(self).__name__
        dict_copy.pop("_sa_instance_state", None)
        return dict_copy
