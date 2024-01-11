#!/usr/bin/python3
"""This module contains a BaseModel parent class"""

from datetime import datetime
import models
import uuid


class BaseModel():
    """This defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Constructor for every new instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String repr of a BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attr"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dict containing keys/values of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
