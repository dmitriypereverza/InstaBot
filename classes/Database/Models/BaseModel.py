#!/usr/bin/python3
# -*- coding: utf-8 -*-

from peewee import Model
from classes.Database.DBConnector import db

class BaseModel(Model):
    class Meta:
        database = db

    def __init__(self):
        super().__init__()
        if not self.table_exists():
            self.create_table()


