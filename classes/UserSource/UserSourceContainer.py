#!/usr/bin/python3
# -*- coding: utf-8 -*-
from itertools import cycle
from  classes.Instagram.InstaBot import InstaBot
from classes.Exeptions.exeptions import NotOverrideMethodExeption
from classes.Instagram.instaUser import User
from classes.UserSource.UserSources import UserList, HashTagUserSource, GeoUserSource, FollowersUserSource

class UserSourceContainer:
    def __init__(self):
        self._sourceConainer = {
            'user_list': UserList,
            'hashTag': HashTagUserSource,
            'geo': GeoUserSource,
            'followers': FollowersUserSource,
        }

    def getUserSource(self, className):
        if className in self._sourceConainer:
            return self._sourceConainer[className]
        else:
            return None