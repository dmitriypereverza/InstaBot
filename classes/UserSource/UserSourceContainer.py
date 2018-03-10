#!/usr/bin/python3
# -*- coding: utf-8 -*-
from classes.UserSource.UserSources import UserList, \
    HashTagUserSource, GeoUserSource, FollowersUserSource

class UserSourceContainer:
    def __init__(self):
        self._sourceConainer = {
            'user_list': UserList,
            'hashTag': HashTagUserSource,
            'geo': GeoUserSource,
            'followers': FollowersUserSource,
        }

    def getUserSource(self, type):
        if type in self._sourceConainer:
            return self._sourceConainer[type]
        else:
            raise Exception('User source type {} not found'.format(type))