#!/usr/bin/python3

""" This file managers the users personal information """
from models.base_model import BaseModel


class User(BaseModel):
    """ All users personal information """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
