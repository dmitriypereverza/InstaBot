#!/usr/bin/python3
# -*- coding: utf-8 -*-
from classes.UserSource.UserSources import UserList, \
    HashTagUserSource, GeoUserSource, FollowersUserSource

FOLLOWERS = 'followers'
GEO = 'geo'
HASH_TAG = 'hashTag'
USER_LIST = 'user_list'

class UserSourceContainer:
    def __init__(self):
        self._sourceConainer = {
            USER_LIST: UserList,
            HASH_TAG: HashTagUserSource,
            GEO: GeoUserSource,
            FOLLOWERS: FollowersUserSource,
        }

    def getUserSource(self, type):
        if type in self._sourceConainer:
            return self._sourceConainer[type]
        else:
            raise Exception('User source type {} not found'.format(type))