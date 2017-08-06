#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Database.DBConnector import *


class BotAccount(Model):
    is_active = BooleanField()
    login = CharField()
    password = CharField()
    user_id = IntegerField()
    token = CharField()
    date_create = DateField()

    def __init__(self):
        super().__init__()
        if not self.table_exists():
            self.create_table()

    class Meta:
        database = db
        db_table = 'acounts'
