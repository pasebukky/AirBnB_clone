#!/usr/bin/python3
"""This module contains a BaseModel parent class"""

from datetime import datetime
import uuid


class BaseModel():
    """This defines all common attributes/methods for other classes"""

    def __init__(self):
        """Constructor for every new instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String representation of a BaseModel instance"""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attr"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dict containing keys/values of __dict__ of the instance"""
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
