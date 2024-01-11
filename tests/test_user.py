#!/usr/bin/python3

""" This file contains all the unittests for the user module """

import models
import os
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """ This is the test class for the user module """
    def initialization(self):
        self.user = User()
        self.user.email = "john_doe29@email.com"
        self.user.password = "john_doe29!"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        storage.new(self.user)
        storage.save()

    def
