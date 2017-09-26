#!/usr/bin/python3
# -*- coding: utf-8 -*-

from peewee import Model, BooleanField, CharField, IntegerField, DateField, ForeignKeyField
from classes.Database.DBConnector import db
from classes.Database.Models.Accounts import Accounts

class TaskSettings(Model):
    class Meta:
        database = db
        db_table = 'task_settings'

    name = CharField()
    account = ForeignKeyField(Accounts, related_name='tasks')

