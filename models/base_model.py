#!/usr/bin/python3
""" BaseModel """

import uuid
from datetime import datetime


class BaseModel:
    """ class from which other classes will inherit from """

    def __init__(self, *args, **kwargs):
        """ Initializes """

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                else:
                    setattr(self, '_BaseModel__class', value)
            self.created_at = datetime.strptime(self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    def __str__(self):
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
