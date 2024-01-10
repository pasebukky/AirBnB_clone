#!/usr/bin/python3

""" This file contains the users reviews """
from models.base_model import BaseModel


class Review(BaseModel):
    """ This contains the review module """
    place_id = ""
    user_id = ""
    text = ""
