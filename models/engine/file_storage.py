#!/usr/bin/python3
"""This module contains the FileStorage class"""

import json
import models
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """
    This class serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """return the __objects dict"""
        return self.__class__.__objects

    def new(self, obj):
        """adds object to __objects dictionary"""
        if obj.id in type(self).__objects:
            return

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__class__.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        serializable_objects = {}

        #__objects contain instances of BaseModel, make them serializable
        for key, value in self.__class__.__objects.items():
            serializable_objects[key] = value.to_dict()

        with open(self.__class__.__file_path, "w") as file:
            json.dump(serializable_objects, file)

    def reload(self):
        """Deserialize JSON file to objects dict, if it exists"""
        if os.path.exists(self.__class__.__file_path):
            try:
                with open(self.__class__.__file_path) as file:
                    for obj in json.load(file).values():
                        #dynamically creates a class obj with it's name
                        #use **unpacking op to unpack remaining keys and values
                        # as args for the new object and add it to __objects
                        self.new(eval(obj["__class__"])(**obj))
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                return
