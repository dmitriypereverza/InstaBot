#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests


class User:
    def __init__(self, userInfo):
        print(userInfo)

        self.id = userInfo['id']
        self.username = userInfo['username']
        self.followsCount = userInfo['follows']['count']
        self.followed_by = userInfo['followed_by']['count']
        self.fullName = userInfo['full_name']
        self.mediaCount = len(userInfo['media']['nodes'])
        self.biography = userInfo['biography']

        self.isFollower = userInfo['follows_viewer'] or userInfo['has_requested_viewer']
        self.isFollowing = userInfo['followed_by_viewer'] or userInfo['requested_by_viewer']

