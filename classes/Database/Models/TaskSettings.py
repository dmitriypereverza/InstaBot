#!/usr/bin/python3
# -*- coding: utf-8 -*-

from peewee import Model, BooleanField, CharField, IntegerField, DateField, ForeignKeyField
from classes.Database.DBConnector import db
from classes.Database.Models.Accounts import Accounts, BaseModel

class Tasks(BaseModel):
    class Meta:
        database = db
        db_table = 'tasks'

    name = CharField()
    account = ForeignKeyField(Accounts, related_name='tasks')
    source_user_list_active = BooleanField(null=True)
    source_user_list_file_path = CharField(null=True)

    source_hashtag_list_active = BooleanField(null=True)
    source_hashtag_list_file_path = CharField(null=True)

    source_geo_list_active = BooleanField(null=True)
    source_geo_list_file_path = CharField(null=True)

    source_follower_list_active = BooleanField(null=True)
    source_follower_list_file_path = CharField(null=True)

    source_follow_by_list_active = BooleanField(null=True)
    source_follow_by_list_file_path = CharField(null=True)

    need_like = BooleanField(null=True)
    first_like = BooleanField(null=True)
    limit_like = IntegerField(null=True)
    count_like = IntegerField(null=True)
    range_like = IntegerField(null=True)

    need_follow = BooleanField(null=True)

    need_comment = BooleanField(null=True)
    comment_file_path = CharField(null=True)

    is_cycleLoop = BooleanField(null=True)


