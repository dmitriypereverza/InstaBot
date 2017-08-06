#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Database.DBConnector import *


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db
        db_table = 'person'
