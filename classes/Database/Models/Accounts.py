#!/usr/bin/python3
# -*- coding: utf-8 -*-

from peewee import Model, BooleanField, CharField, IntegerField, DateField
from classes.Database.Models.BaseModel import BaseModel

class Accounts(BaseModel):
    is_active = BooleanField(default=False)
    login = CharField()
    password = CharField()
    img_url = CharField()
    user_id = IntegerField()
    token = CharField(default=None)
    date_create = DateField()

    def getAllAccounts(self):
        return self.select()
