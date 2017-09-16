#!/usr/bin/python3
# -*- coding: utf-8 -*-

from peewee import Model, BooleanField, CharField, IntegerField, DateField
from classes.Database.DBConnector import db

class BotAccount(Model):
    class Meta:
        database = db
        db_table = 'acounts'

    is_active = BooleanField(default=False)
    login = CharField()
    password = CharField()
    img_url = CharField()
    user_id = IntegerField()
    token = CharField(default=None)
    date_create = DateField()

    def __init__(self):
        super().__init__()
        if not self.table_exists():
            self.create_table()

    def getAllAccounts(self):
        return self.select()
