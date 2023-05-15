#!/usr/bin/python3
""" module for file storage class """

import json
import os.path

class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, file)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as file:
                data = json.load(file)
                for k, v in data.items():
                    module, obj_id = k.split(".")
                    cls = globals()[module]
                    obj = cls(**v)
                    FileStorage.__objects[k] = obj
