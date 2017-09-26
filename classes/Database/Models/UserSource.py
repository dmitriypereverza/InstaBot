#!/usr/bin/python3
# -*- coding: utf-8 -*-

from peewee import Model, CharField, ForeignKeyField
from classes.Database.Models.TaskSettings import TaskSettings

class UserSource(Model):
    name = CharField()
    task = ForeignKeyField(TaskSettings, related_name='user_sources')
