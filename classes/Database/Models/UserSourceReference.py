#!/usr/bin/python3
# -*- coding: utf-8 -*-

from peewee import Model, CharField, ForeignKeyField
from classes.Database.Models.UserSource import UserSource

class UserSourceValue(Model):
    userSource = ForeignKeyField(UserSource, related_name='values')
    value = CharField()
